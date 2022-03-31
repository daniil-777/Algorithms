import pytest
import pandas as pd
from collections import OrderedDict

from .roi import compute_roi


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
            coins=pd.DataFrame(
                data=[
                    ['BTC', 7456.41, '2018-04-04'],
                    ['LTC', 133.91, '2018-04-04'],
                    ['BTC', 7500.7, '2018-06-01'],
                    ['LTC', 118.03, '2018-06-01']
                ],
                columns=['symbol', 'price', 'date'],
                index=pd.to_datetime(
                    ['2018-04-04', '2018-04-04', '2018-06-01', '2018-06-01'])
            ),
            investments={'BTC': 1000, 'LTC': 500},
            start_date='2018-04-04',
            end_date='2018-06-01',
            expected=-0.035569133065275614
        )
    )
])


@pytest.mark.parametrize(
    'test_case',
    TEST_CASES.values(),
    ids=list(TEST_CASES.keys())
)
def test_compute_roi(test_case):
    roi = compute_roi(
        test_case.coins,
        test_case.investments,
        test_case.start_date,
        test_case.end_date)
    assert pytest.approx(roi, rel=1e-3) == test_case.expected
