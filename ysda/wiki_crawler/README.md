Напишите краулер (программу, обходящую заданный сегмент интернета по ссылкам), который должен обойти статьи википедии (предположительно румынской), достижимые со [стартовой страницы](http://rmy.wikipedia.org).
Для каждой найденной статьи посчитатайте её удалённость от главной страницы. Удалённость стартовой страницы равна 0. Если на страницу можно попасть разными способами, берите кратчайшее расстояние.
В `crawler.py` переопределите словарь `WIKI_PAGE_DEPTHS`
```json
{
    "<title 1>": <deepth>,
    "<title 2>": <deepth 2>
}
```

где title – атрибут страницы в BeautifulSoup извлекаемый из
```python
soup.findAll('a', attrs={"dir": "ltr"})[0].text
```

Пример:
```json
{
    "Sherutni_patrin": 0,
    "Romano_lekhipen": 1,
    "Sinti": 1
}
```

* Служебные ссылки и ссылки на несуществующие страницы не должны войти в ответ.
* Чекер толерантен к некоторому отклонению в количестве найденных страниц, но не толерантен к альтернативным кодировкам и отклонениям в записи заголовков.
* Для скачивания странички пользуйтесь библиотекой `requests`, для парсинга html – `BeautifulSoup`.
* Всего статей примерно 300, работать кроулер должен совсем не долго.