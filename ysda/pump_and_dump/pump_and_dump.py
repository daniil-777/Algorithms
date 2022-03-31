import pandas as pd


def find_most_severe_pump_and_dump(
    coins: pd.DataFrame, symbol: str, start_date: str, end_date: str
) -> dict:
    """
    :param coins: coins open, close, high prices (in USD)
    and names for each date
    :param symbol: name of the traded coin
    :param start_date: begining of the date range
    :param end_date: end of the date range
    :return: date and value of maximal pump and dump
    """
    coins_new = coins.loc[start_date:end_date]
    coins_new1 = coins_new[coins_new['symbol'] == symbol]
    coins_new1['new'] = coins_new1['high'] / coins_new1[['open', 'close']].max(axis=1)
    coins_new1.sort_values(by=['new'], kind='quicksort', inplace=True)
    pnd = float(coins_new1.iloc[-1]['new'])
    data = str(coins_new1.iloc[-1]['date'])
    d = {}
    d['date'] = data
    d['pnd'] = pnd
    return d
