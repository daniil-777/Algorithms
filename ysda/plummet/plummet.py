import pandas as pd


def find_toughest_plummet(
    coins: pd.DataFrame, symbol: str, start_date: str, end_date: str
) -> dict:
    """
    :param coins: coins price (in USD) and names for each date
    :param symbol: name of the traded coin
    :param start_date: begining of the date range
    :param end_date: end of the date range
    :return: date and value of maximal plummet
    """
    coins_new = coins.loc[start_date:end_date]
    coins_new1 = coins_new[coins_new['symbol'] == symbol]
    coins_new1 = coins_new1.copy()
    coins_new1.loc[:, 'new'] = coins_new1.price.pct_change()
    coins_new1 = coins_new1.dropna()
    if coins_new1['new'].min() > 0:
        coins_new1.sort_values(by=['new'], kind='quicksort', inplace=True)
    else:
        coins_new1 = coins_new1[coins_new1['new'] < 0]
        coins_new1.sort_values(by=['new'], kind='quicksort', inplace=True)
    pnd = float(coins_new1.iloc[0]['new']*100)
    data = str(coins_new1.iloc[0]['date'])
    d = {}
    d['date'] = data
    d['plummet'] = pnd
    return d


find_toughest_plummet(
     pd.DataFrame(
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
     end_date='2017-11-03'
 )
