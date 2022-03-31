## Крах

### Условие

Критовалюты это далеко не всегда большие доходы и огромные прибыли. Волатильность может играть и против вас, например, когда цена очень сильно падает.
Вам нужно для заданного диапазона дат найти день когда цена упала сильнее всего, по сравнению с предыдущим днем и величину этого падения (в процентах). 
Примечание: для первой даты диапазона падение находить не нужно. Если цена монеты все время росла найдите день когда рост был минимальным и величину роста
в процентах.

### Формат входных и выходных данных

Вам нужно в файле ```plummet.py``` реализовать функцию ``find_toughest_plummet``, на вход которой подается
 - Объект DataFrame со следующими данными
    - индекс содержащий даты
    - колонка symbol - сокращенное название монеты
    - колонка date - строковое представление даты (в формате YYYY-mm-dd)
    - колонка price - цена монеты в указанную дату в USD
 - Строка с сокращенным названием торгуемой монеты
 - Строка с датой начала диапазона (в формате YYYY-mm-dd)
 - Строка с датой конца диапазона (в формате YYYY-mm-dd)

На выходе - словарь с двумя ключами: 'date' и 'plummet'. По ключу 'date' хранится дата в формате YYYY-mm-dd, по ключу 'plummet' - действительное число 
с относительной ошибкой не более 0.001. Входные данные могут содержать лишние даты, монеты и колонки.

### Пример
```
>>> find_toughest_plummet(
...     pd.DataFrame(
...         data=[
...             ['ADA', 0.029126999999999997, '2017-11-01'],
...             ['ADA', 0.023079, '2017-11-02'],
...             ['ADA', 0.021418, '2017-11-03']
...         ],
...         columns=['symbol', 'price', 'date'],
...         index=pd.to_datetime(['2017-11-01', '2017-11-02', '2017-11-03'])
...     ), 
...     symbol='ADA',
...     start_date='2017-11-01',
...     end_date='2017-11-03'
... )
{'date': '2017-11-02', 'plummet': -20.764239365537129}
```