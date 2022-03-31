# Декоратор проверки аргументов

Напишите декоратор `@takes`, который будет проверять правильность типов входных аргументов функции. 

Декоратор принимает на вход типы аргументов и декорирует функцию таким образом, что она генеририрует
исключение `TypeError`, если хотя бы один из аргументов имеет неверный тип. 
            
Если аргументов больше, чем типов, то ошибку генерировать не нужно (возможно, точный тип известен
только для первых аргументов, его, как раз, надо проверить). 
            
Если типов больше, чем аргументов, то это тоже ошибка только в случае, если переданные аргументы
не подходят под соответствующие им по порядку типы (например, декоратор может быть применен к функциям
с переменным числом аргументов).

Важно помнить про [**наследование типов**](https://ru.wikipedia.org/wiki/Наследование_(программирование)),
т.е. если в функцию передали тип `Number`, являющийся потомком `int`, а в декораторе указан `int`,
то декоратор должен разрешать такое поведение. Каноничным способом проверить тип в питоне с учетом наследования: 
[`isinstance`](https://docs.python.org/3.6/library/functions.html#isinstance).

Декоратор должен вести себя порядочно, то есть не должен затирать основные атрибуты функции:
`__name__`, `__doc__`, `__module__`.

Для простоты можно считать, что у функции нет именованных аргументов.
Генерацию исключений воспринимайте пока как волшебный способ просигнализировать об ошибке.
Делается это так: `raise TypeError()`


### Пример

```
>>> @takes(int, str)
... def f(a, b):
...     pass
... 
>>> f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "~/shad-py/check_deco/check_deco.py", line 10, in wrapper
    raise TypeError()
TypeError
```