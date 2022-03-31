import pytest
import pandas as pd
from collections import OrderedDict

from .pump_and_dump import find_most_severe_pump_and_dump


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
                    ['FUN', 0.014053, 0.01860999, 0.022747, '2017-06-28'],
                    ['FUN', 0.018567, 0.020344, 0.254108, '2017-06-29'],
                    ['FUN', 0.020367, 0.03314100, 0.148304, '2017-06-30']
                ],
                columns=['symbol', 'open', 'close', 'high', 'date'],
                index=pd.to_datetime(['2017-06-28', '2017-06-29', '2017-06-30'])
            ),
            symbol='FUN',
            start_date='2017-06-28',
            end_date='2018-06-30',
            expected={'date': '2017-06-29', 'pnd': 12.490562327959102}
        )
    )
])


@pytest.mark.parametrize(
    'test_case',
    TEST_CASES.values(),
    ids=list(TEST_CASES.keys())
)
def test_find_most_severe_pump_and_dump(test_case):
    scam_info = find_most_severe_pump_and_dump(
        test_case.coins,
        test_case.symbol,
        test_case.start_date,
        test_case.end_date)
    assert scam_info['date'] == test_case.expected['date']
    assert pytest.approx(scam_info['pnd'], rel=1e-3) == \
        test_case.expected['pnd']
