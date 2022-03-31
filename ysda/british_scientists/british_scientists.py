import re


def shuffle_text(text: str, letters_to_shuffle: int) -> str:
    new = ""
    prev_pos = 0
    for next in re.finditer('(\\w[^\\d\\s\\W]+)+', text):
        word_pos = next.span(0)
        new += text[prev_pos:word_pos[0]]
        prev_pos = word_pos[1]
        word = text[word_pos[0] + 1:word_pos[1] - 1]
        shuffled_length = min(letters_to_shuffle, len(word))
        shuffled_part = ''.join(reversed(word[:shuffled_length]))
        word = text[word_pos[0]] + shuffled_part + text[word_pos[0] + 1 + shuffled_length:word_pos[1]]
        new += word
    new += text[prev_pos:]
    return new
