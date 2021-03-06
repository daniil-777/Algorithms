## ЛИСТ ТВИСТ

### Пререквизиты

Python версии 3.6.3. Pytest версии 3.2.3.

### Условие

Вам нужно в файле ```list_twist.py``` реализовать класс с интерфейсом списка, в котором добавить аттрибуты:
* **reversed** (с коротким псевдонимом **R**):
  * При обращении возвращается список с элементами в обратном порядке.
* **first** (с коротким псевдонимом **F**):
  * При обращении возвращается первый элемент списка. 
  * Должна присутствовать возможность изменять этот атрибут. Вместе с ним должен меняться и сам список
  * При попытке доступиться или установить **first** в пустом списке поведение не определено
* **last** (с коротким псевдонимом **L**):
  * При обращении возвращается последний элемент списка.
  * Должна присутствовать возможность изменять этот атрибут. Вместе с ним должен меняться и сам список. 
  * При попытке доступиться или установить **last** в пустом списке поведение не определено
* **size** (с коротким псевдонимом **S**):
  * При обращении возвращается размер списка. 
  * Должна присутствовать возможность изменять этот атрибут: 
    при увеличении размера в конец должны добавляться значения None, 
    а при уменьшении последние элементы должны удаляться.

### Замечания

* Все перечисленные атрибуты не являются методами (см. пример)
* Нужно вычислять на лету и модифицировать состояние
* Обратите внимание на алиасинг. Если использовать ```property```, то под каждый из алиасов нужно будет заводить отдельную проперти.
Поэтому нужно разобраться с ```__getattr__``` и ```__setattr__```
* Прочитайте внимательно про правила реализации интерфейса [UserList](https://docs.python.org/3.6/library/collections.html#collections.UserList)
* Важно не сломать базовую функциональность списка

## Пример

Прочитайте в первую очередь описание, пример чисто для справки.

```python
>>> list_twist = ListTwist([1, 2, 3])
>>> print(list_twist.reversed)
[3, 2, 1]
>>> print(list_twist.first)
1
>>> list_twist.F = 0
>>> print(list_twist)
[0, 2, 3]
>>> print(list_twist.last)
3
>>> list_twist.last = 4
[0, 2, 4]
>>> list_twist.size = 2
>>> print(list_twist)
[0, 2]
>>> list_twist.size = 4
>>> print(list_twist)
[0, 2, None, None]
```

### Пример запуска тестов
Запускаются тесты из файла ```test_public.py```. Стоит добавить туда своих кейзов для проверки функции перед сабмитом.
```bash
ilariia@ilariia-osx1:~/shad-py/list_twist(master)$ ~/.pyenv/versions/3.6.3/bin/pytest .
```
