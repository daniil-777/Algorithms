import pandas as pd
import numpy as np


def compute_volatility(
    coins: pd.DataFrame, investments: dict, start_date: str, end_date: str
) -> float:
    """
    :param coins: coins price (in USD) and names for each date
    :param investments: mapping from coin names to investments (in USD)
    :param start_date: buy date
    :param end_date: sell date
    :return: standard deviation of portfolio value
    """
    coins_new = coins.loc[start_date:end_date]
    profile = []
    coins = coins.sort_index()
    for coin, invest in investments.items():
        coin_price = coins.loc[coins['symbol'] == coin, 'price']
        start = coin_price.loc[start_date]
        coins_count = invest / start
        change = coin_price.loc[start_date:end_date].values
        profile.append(change * coins_count)
    return np.var(sum(profile), ddof=1) ** (1 / 2)
