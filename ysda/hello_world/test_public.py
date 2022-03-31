import pytest
from .hello_world import get_hello_world


class Case(object):
    def __init__(self, name, expected):
        self.name = name
        self.expected = expected

    def __str__(self):
        return "test_{}".format(self.name)


TEST_CASES = [
    Case(name="basic", expected="Hello world!")
]


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_nearest_happy_ticket(test_case):
    answer = get_hello_world()
    assert answer == test_case.expected
