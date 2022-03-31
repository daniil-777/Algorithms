import functools
from datetime import datetime

from lru_cache import cache


@cache(20)
def binomial(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    return binomial(n - 1, k) + binomial(n - 1, k - 1)


def test_binomial():
    result = sum(binomial(30, i) for i in range(31))
    assert result == 2 ** 30
