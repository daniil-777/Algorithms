import pytest
import pandas as pd
from collections import OrderedDict

from .plummet import find_toughest_plummet


class Case(object):
    def __init__(self, coins, symbol, start_date, end_date, expected):
        self.coins = coins
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.expected = expected


TEST_CASES = OrderedDict([
    (
        "test_case_0",
        Case(
            coins=pd.DataFrame(
                data=[
                    ['ADA', 0.029126999999999997, '2017-11-01'],
                    ['ADA', 0.023079, '2017-11-02'],
                    ['ADA', 0.021418, '2017-11-03']
                ],
                columns=['symbol', 'price', 'date'],
                index=pd.to_datetime(['2017-11-01', '2017-11-02', '2017-11-03'])
            ),
            symbol='ADA',
            start_date='2017-11-01',
            end_date='2017-11-03',
            expected={'date': '2017-11-02', 'plummet': -20.764239365537129}
        )
    )
])


@pytest.mark.parametrize(
    'test_case',
    TEST_CASES.values(),
    ids=list(TEST_CASES.keys())
)
def test_find_toughest_plummet(test_case):
    info = find_toughest_plummet(
        test_case.coins,
        test_case.symbol,
        test_case.start_date,
        test_case.end_date)
    assert info['date'] == test_case.expected['date']
    assert pytest.approx(info['plummet'], rel=1e-3) == \
        test_case.expected['plummet']
