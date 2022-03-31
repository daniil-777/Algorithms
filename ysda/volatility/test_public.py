import pytest
import pandas as pd
from collections import OrderedDict

from .volatility import compute_volatility


class Case(object):
    def __init__(self, coins, investments, start_date, end_date, expected):
        self.coins = coins
        self.investments = investments
        self.start_date = start_date
        self.end_date = end_date
        self.expected = expected


TEST_CASES = OrderedDict([
    (
        "test_case_0",
        Case(
            pd.DataFrame(
                data=[
                    ['ETH', 416.48, '2018-04-04'],
                    ['NEO', 53.38, '2018-04-04'],
                    ['ETH', 578.67, '2018-06-01'],
                    ['NEO', 53.2, '2018-06-01']],
                columns=['symbol', 'price', 'date'],
                index=pd.to_datetime(
                    ['2018-04-04', '2018-04-04', '2018-06-01', '2018-06-01'])
            ),
            investments={'NEO': 1000, 'ETH': 2000},
            start_date='2018-04-04',
            end_date='2018-06-01',
            expected=548.35344595230993
        )
    )
])


@pytest.mark.parametrize(
    'test_case',
    TEST_CASES.values(),
    ids=list(TEST_CASES.keys())
)
def test_compute_volatility(test_case):
    volatility = compute_volatility(
        test_case.coins,
        test_case.investments,
        test_case.start_date,
        test_case.end_date)
    assert pytest.approx(volatility, rel=1e-3) == test_case.expected
