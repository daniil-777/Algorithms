import pytest

from .fantics import get_combinations


class Case(object):
    def __init__(self, total_fantics, values, expected):
        self.total_fantics = total_fantics
        self.values = values
        self.expected = expected

    def __str__(self):
        return "test_{}_fantics_with_{}".format(
            self.total_fantics,
            ",".join(str(i) for i in self.values)
        )


TEST_CASES = [
    Case(total_fantics=1, values={1, 5, 10}, expected=1),
]


@pytest.mark.parametrize("test_case", TEST_CASES,
                         ids=[str(t) for t in TEST_CASES])
def test_fantics(test_case):
    combinations = get_combinations(test_case.total_fantics, test_case.values)
    assert combinations == test_case.expected
