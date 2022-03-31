import pandas as pd


def luck_factor(
    coins: pd.DataFrame, symbol: str, start_date: str, end_date: str
) -> float:
    """
    :param coins: coins low, high prices (in USD) and names for each date
    :param symbol: name of the traded coin
    :param start_date: first day of trading
    :param end_date: last day of trading
    :return: investments growth factor
    """
    coins_new = coins.loc[start_date:end_date]
    coins_new1 = coins_new[coins_new['symbol'] == symbol]
    result = 1
    for index, row in coins_new1.iterrows():
        result *= float(row['high'])/float(row['low'])
    return result
