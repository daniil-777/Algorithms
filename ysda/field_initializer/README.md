## Инициализатор
Ваша задача написать метакласс `FieldInitializer`, который позволит избавиться от лишнего boilerplate кода при инициализации инстанса класса:
```python
def __init__(self, value=value):
    self.value = value
```
Если полей много -- это унылый процесс.

### Пример использования:
```python
class A(metaclass=FieldInitializer):
    pass

a = A(foo=42)
assert a.foo == 42

class B(metaclass=FieldInitializer):
    def __init__(self, a, b, c, d=1):
        self.a = 1
        self.b = b
        self.d = d + 1

b = B(1, 2, 3, foo=4, d=5)
assert b.a == 1
assert b.b == 2
assert b.foo == 4
assert b.d == 6
try:
    _ = b.c
except AttributeError:
    print('all correct')
else:
    assert False, 'error'
```

Т.е. метакласс берёт все keyword аргументы инициализатора и создаёт в инстансе класса атрибуты с соответствующими именами и значениями.

#### P.S
Обратите внимание на то, что данный метакласс не должен менять поля, которые и так есть в спеке/классе