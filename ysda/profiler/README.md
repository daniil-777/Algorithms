# Профилятор

Напишите декоратор `@proﬁler`, который при вызове функции будет сохранять в её атрибуты
время ее исполнения (в секундах, можно дробное) и количество рекусивных вызовов произошедших при **последнем** вызове функции.
Атрибуты назовите `last_time_taken` и `calls`.

Пользоваться глобальными переменными запрещено.
Декоратор должен вести себя порядочно, то есть не должен затирать основные атрибуты функции:
`__name__`, `__doc__`, `__module__`.

### Пример

```
>>> @profiler
... def f():
...     pass
... 
>>> f()
>>> f()
>>> f.calls
1
>>> f.last_time_taken
3.7e-05
```

## Примечания
Проверить работу вашего декоратора стоит на [функции Аккермана](https://ru.wikipedia.org/wiki/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F_%D0%90%D0%BA%D0%BA%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B0),
она уже реализована в публичных тестах.