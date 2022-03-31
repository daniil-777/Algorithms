from british_scientists import shuffle_text


def check_shuffled(shuffled, original):
    shuffled = ''.join([c for c in shuffled if c.isalpha() or c.isspace()])
    original = ''.join([c for c in original if c.isalpha() or c.isspace()])
    checks_failed = 0
    checks_total = 0
    for shuffled_word, original_word in zip(shuffled.split(), original.split()):
        if len(original_word) < 4:
            continue
        checks_total += 1
        checks_failed += (shuffled_word == original_word)
    assert checks_failed <= round(checks_total * 0.2)


def test_simple():
    etalon = 'OhhHhh my PytHon 3! like it ;)'
    assert shuffle_text(etalon, 0) == etalon
    assert shuffle_text(etalon, 1) == etalon
    check_shuffled(shuffle_text(etalon, 2), etalon)


def test_zen():
    etalon = (
            "The Zen of Python, by Tim Peters"
            ""
            "Прекрасное лучше уродливого."
            "Explicit is better than implicit."
            "Simple is better than complex."
            "Complex is better than complicated."
            "Flat is better than nested."
            "Sparse is better than dense."
            "Readability counts."
            "Special cases aren't special enough to break the rules."
            "Although practicality beats purity."
            "Errors should never pass silently."
            "Unless explicitly silenced."
            "In the face of ambiguity, refuse the temptation to guess."
            "There should be one-- and preferably only one --obvious way to do it."
            "Although that way may not be obvious at first unless you're Dutch."
            "Now is better than never."
            "Although never is often better than *right* now."
            "If the implementation is hard to explain, it's a bad idea."
            "If the implementation is easy to explain, it may be a good idea."
            "Namespaces are one honking great idea -- let's do more of those!"
        )
    assert shuffle_text(etalon, 1) == etalon
    check_shuffled(shuffle_text(etalon, 3), etalon)


def test_random():
    etalon = (
            "QwwwwwwwQ-- aaaaa -- SrrrS..."
            "aZZZZZZa!!!!!! '1bb7',     qw"
            "wq. NnnnnnnnnN wer? 1llllllll7!"
        )
    assert shuffle_text(etalon, 1) == etalon
    assert shuffle_text(etalon, 42) == etalon
