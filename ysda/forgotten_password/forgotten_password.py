from typing import List

import itertools


def generate_passwords(words: str) -> List[str]:
    result = []
    a = words.split()
    q = len(a) + 1
    for j in range(1, q):
        for item in list(itertools.permutations(a, j)):
            s = ''.join(item)
            result.append(s)
    result.sort()
    return result
