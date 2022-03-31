## ОБОБЩЕННЫЙ ФИБОНАЧЧИ

### Пререквизиты

Python версии 3.6.3. Pytest версии 3.2.3.

### Условие

Вам нужно реализовать функцию в файле ```fibonacci.py```, на вход которой дана позиция в [ряде Фибоначчи](https://ru.wikipedia.org/wiki/Числа_Фибоначчи),
первое и второе число последовательности, а на выходе - значение n-го числа в ряде.  
Знаем, что позиция, которую будут хотеть извлекать, не больше 1000. А начальные элементы последовательности - целые числа.

### Пример
```python
>>> get_fibonacci_value(1, 0, 1)
1
```

### Пример запуска тестов
Запускаются тесты из файла ```test_public.py```. Стоит добавить туда своих кейзов для проверки функции перед сабмитом.
```bash
ilariia@ilariia-osx1:~/shad-py/fibonacci(master)$ ~/.pyenv/versions/3.6.3/bin/pytest .
```