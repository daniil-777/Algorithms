import pytest
import pandas as pd
from collections import OrderedDict

from .luck import luck_factor


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
                    ['BTC', 15404.8, 17513.9, '2017-12-11'],
                    ['BTC', 16571.6, 17781.8, '2017-12-12'],
                    ['BTC', 16039.7, 17653.1, '2017-12-13']],
                columns=['symbol', 'low', 'high', 'date'],
                index=pd.to_datetime(['2017-12-11', '2017-12-12', '2017-12-13'])
            ),
            symbol='BTC',
            start_date='2017-12-11',
            end_date='2017-12-13',
            expected=1.342650014778795
        )
    )
])


@pytest.mark.parametrize(
    'test_case',
    TEST_CASES.values(),
    ids=list(TEST_CASES.keys())
)
def test_luck_factor(test_case):
    factor = luck_factor(
        test_case.coins,
        test_case.symbol,
        test_case.start_date,
        test_case.end_date)
    assert pytest.approx(factor, rel=1e-3) == test_case.expected
