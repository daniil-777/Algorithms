from typing import Iterable


def flat_it(sequence: Iterable):
    try:
        for elem in sequence:
            if elem != sequence:
                yield from flat_it(elem)
            else:
                yield elem
    except TypeError:
        yield sequence
