import re
import math
from collections import Counter
from operator import itemgetter
from setup import Graph, Input, Reduce, Map, Sort, Join, Fold


def split_text(record):
    """
    Split rows with 'text' field into set of rows with 'token' field
    (one for every  occurence of every word in text)
    """
    new_text = re.sub('[^A-Za-z]+', ' ', record['text'])
    tokens = new_text.split()
    for token in tokens:
        yield {
            'doc_id': record['doc_id'],
            'word': token.lower(),
        }

def count_words_in_doc(rows):
    """ Count words in doc. """
    rows[0].update({"number_in_doc": len(rows)})
    yield rows[0]


def count_sum_of_docs(rows):
    """ Count sum of docs. """
    flag = True
    if len(rows) < rows[0]['number_of_docs']:
        flag = False

    for row in rows:
        if row['number_in_doc'] < 2:
            flag = False

    if flag:
        sum_of_docs = sum(row['number_in_doc'] for row in rows)
        for row in rows:
            row.update({"sum_of_docs": sum_of_docs})
            yield row


def docs_count(state, record):
    """ Increment of docs_count """
    return {"docs_count": state["docs_count"] + 1}


def word_counter(rows):
    """ Count words. """
    yield {
        'text': rows[0]['word'],
        'count': len(rows)
    }


def unique(records):
    """ Convolve records with similar key to one record. """
    yield records[0]


def calc_idf(records):
    """ Calculate idf. """
    doc_counter = Counter()
    for row in records:
        doc_counter[row['word']] += 1

    for w, count in doc_counter.items():
        yield {
            "word": row["word"],
            "count_idf": count,
            "docs_count": row["docs_count"]
        }


def term_frequency_reducer(records):
    """ Calculate term frequency for every word in doc_id. """
    word_count = Counter()
    for row in records:
        word_count[row['word']] += 1

    total = sum(word_count.values())

    for w, count in word_count.items():
        yield {
            'doc_id': row['doc_id'],
            'word': w,
            'tf': count / total
        }


def invert_index(records):
    """ Calculate final result. """
    for row in records:
        row["tf_idf"] = row["tf"] * \
                        math.log(row['docs_count'] / row['count_idf'])

    records = sorted(records, key = itemgetter("tf_idf"), reverse=True)

    yield {
        "word": row["word"],
        "index": [(records[i]["doc_id"], records[i]["tf_idf"])
                  for i in range(0, min(3, len(records)))]
    }


def count_words(rows):
    """ Count total number of word occurrence in all docs. """
    number = sum(row['words_in_doc'] for row in rows)
    for row in rows:
        row.update({"words_in_total": number})
        yield row


def count_words_in_one_doc(rows):
    """ Count number of word occurrence in one doc. """
    number = sum(row['number_in_doc'] for row in rows)
    for row in rows:
        row.update({"words_in_doc": number})
        yield row


def count_pmi(rows):
    """ Calculate PMI and yield result. """
    words = []
    for row in rows:
        pmi = math.log(row['number_in_doc'] * row['words_in_total']
                       / row['sum_of_docs'] / row['words_in_doc'])

        words.append((row['word'], pmi))

    words.sort(key=lambda x: x[1], reverse=True)
    yield {
        'doc_id': rows[0]['doc_id'],
        'top_words': words[:10]
    }


def build_word_count_graph(input_stream):
    input_node = Input(input_stream)
    mapper = Map(split_text)(input_node)
    sort = Sort("word")(mapper)
    reduce = Reduce(word_counter, "word")(sort)

    graph = Graph(input_node=input_node, output_node=reduce)
    graph.run(input_file="resource/text_corpus.txt",
              output_file=open("word_count.txt", "w"))


def build_inverted_index_graph(input_stream, doc_column='doc_id', text_column='text'):
    split_input_node = Input()
    split_mapper = Map(split_text)(split_input_node)
    split_words = Graph(input_node=split_input_node, output_node=split_mapper,
                        name="split_words")

    fold_input = Input()
    folder = Fold(docs_count, {"docs_count": 0}, "doc_number")(fold_input)
    count_docs = Graph(input_node=fold_input, output_node=folder)

    count_idf_input = Input(split_words)
    sort_node = Sort([doc_column, "word"])(count_idf_input)
    reducer = Reduce(unique, [doc_column, "word"])(sort_node)
    join = Join(count_docs, [], "outer")(reducer)
    sort_by_word = Sort("word")(join)
    count_idf_reducer = Reduce(calc_idf, ["word"])(sort_by_word)
    count_idf = Graph(input_node=count_idf_input,
                      output_node=count_idf_reducer)

    calc_index_input = Input(split_words)
    sort_doc = Sort(doc_column)(calc_index_input)
    tf_reducer = Reduce(term_frequency_reducer, doc_column)(sort_doc)
    join_left = Join(count_idf, "word", "left")(tf_reducer)
    invert_reduce = Reduce(invert_index, "word")(join_left)
    calc_index = Graph(input_node=calc_index_input, output_node=invert_reduce)

    dependencies = {
        split_words: "data/text_corpus.txt",
        count_docs: "data/text_corpus.txt",
    }

    res = calc_index.run(inputs=dependencies,
                         output_file=open("tf-idf.txt", "w"))


def build_pmi_graph(input_stream, doc_column='doc_id', text_column='text'):
    input_node = Input()
    docs_count_reducer = Reduce(docs_count)(input_node)
    split_mapper = Map(split_text, "tokenizer")(docs_count_reducer)
    sort_by_word_doc_id = Sort(by=['word', 'doc_id'])(split_mapper)

    words_in_doc_reducer = Reduce(count_words_in_doc, key=('word',
                                                           'doc_id'))(sort_by_word_doc_id)

    sum_of_docs = Reduce(count_sum_of_docs,
                         key=('word'))(words_in_doc_reducer)

    sort_by_doc_id = Sort(by="doc_id")(sum_of_docs)

    word_in_one_doc_reducer = Reduce(count_words_in_one_doc,
                                     key="doc_id")(sort_by_doc_id)

    words_reducer = Reduce(count_words)(word_in_one_doc_reducer)
    pmi_reducer = Reduce(count_pmi, "doc_id")(words_reducer)

    graph = Graph(input_node=input_node, output_node=pmi_reducer)

    res = graph.run(input_file="data/text_corpus.txt",
                        output_file=open("pmi.txt", "w"))


def build_yandex_maps_graph(input_stream, input_stream_length):
    pass





