import pytest


from .fibonacci import get_fibonacci_value


class Case(object):
    def __init__(self, position: int, first_value: int,
                 second_value: int, expected: int):
        self.position = position
        self.expected = expected
        self.first_value = first_value
        self.second_value = second_value

    def __str__(self):
        return "test_{}".format(self.position)


TEST_CASES = [
    Case(position=1, first_value=0, second_value=1, expected=1)
]


@pytest.mark.parametrize("test_case", TEST_CASES,
                         ids=[str(t) for t in TEST_CASES])
def test_fibonacci(test_case: Case):
    combinations = get_fibonacci_value(
        test_case.position, test_case.first_value, test_case.second_value
    )
    assert combinations == test_case.expected
