import pandas as pd


def compute_roi(
    coins: pd.DataFrame, investments: dict, start_date: str, end_date: str
) -> float:
    """
    :param coins: coins price (in USD) and names for each date
    :param investments: mapping from coin names to investments (in USD)
    :param start_date: buy date
    :param end_date: sell date
    :return: return of investments (ROI)

    """
    end = 0
    begin = 0
    for key, value in investments.items():
        a = float(coins[(coins['date'] == start_date) & (coins['symbol'] == key)]['price'])
        b = float(coins[(coins['date'] == end_date) & (coins['symbol'] == key)]['price'])
        end += (value / a) * b
        begin += value
    result = (end - begin)/begin
    return result


if __name__ == '__main__':
    coins = pd.DataFrame(
        data=[
            ['BTC', 7456.41, '2018-04-04'],
            ['LTC', 133.91, '2018-04-04'],
            ['BTC', 7500.7, '2018-06-01'],
            ['LTC', 118.03, '2018-06-01']
        ],
        columns=['symbol', 'price', 'date'],
        index=pd.to_datetime(
            ['2018-04-04', '2018-04-04', '2018-06-01', '2018-06-01'])
    )
    investments = {'BTC': 1000, 'LTC': 500}
    start_date = '2018-04-04'
    end_date = '2018-06-01'
    e = compute_roi(coins, investments, start_date, end_date)
    print(e)
