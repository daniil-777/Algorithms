## СЧАСТЛИВЫЙ БИЛЕТ


### Пререквизиты

Python версии 3.6.3. Pytest версии 3.2.3.

### Условие

Номер билета может состоять из 6 любых цифр.
Счастливый билет - это билет, у которого сумма первых трех цифр равна сумме последних трех цифр.

Вам нужно реализовать функцию в файле ```biletik.py```, на вход которой приходит строка с номером билета.
А на выход - строка с ближайшим к нему счастливым билетом.

### Пример
```python
>>> get_nearest_happy_ticket("228419")
"228417"
```

### Пример запуска тестов
Запускаются тесты из файла ```test_public.py```. Стоит добавить туда своих кейзов для проверки функции перед сабмитом.
```bash
ilariia@ilariia-osx1:~/shad-py/biletik(master)$ ~/.pyenv/versions/3.6.3/bin/pytest .
```
