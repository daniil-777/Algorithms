import pytest
from collections import OrderedDict

from .fizz_buzz import get_fizz_buzz


class Case(object):
    def __init__(self, n, expected):
        self.n = n
        self.expected = expected


TEST_CASES = OrderedDict([
    ("test_case_1", Case(n=2, expected={0: 1, 1: 2}))
    
])



@pytest.mark.parametrize("test_case", TEST_CASES.values(),
                         ids=list(TEST_CASES.keys()))
def test_get_fizz_buzz(test_case):
    fizz_buzz_list = get_fizz_buzz(test_case.n)
    assert len(fizz_buzz_list) == test_case.n
    for key, value in test_case.expected.items():
        assert fizz_buzz_list[key] == value
