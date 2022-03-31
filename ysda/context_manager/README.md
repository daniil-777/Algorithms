## Контекстные менеджеры

### Условие

Чудесная штука – исключения. В комплекте же с контекстными менеджерами их возможности возрастают многократно.

Напишите несколько контекстных менеджеров для обработки исключений.

#### Глушитель исключений
```python
with supresser(type_one, ...):
    do_smth()
```

перехватывает исключения заданых (и только заданных) типов и возвращает управление потоку. Исключение не пробрасывается дальше

#### Переименователь исключений
```python
with retyper(type_from, type_to):
    do_smth()
```

меняет тип исключения, оставляя неизменными содержимое ошибки (атрибут args) и трейсбек. Исключение пробрасывается дальше

#### Дампер исключений
```python
with dumper(stream):
    do_smth()
```

записывает в переданный поток сообщение об ошибке и пробрасывает его дальше. 

Поток - это наследник [TextIOBase](https://docs.python.org/2/library/io.html#io.TextIOBase). 
Например, ```sys.stderr``` и ```io.StringIO``` - это наследники TextIOBase, поэтому у них есть метод write.

### Уточнения

* Нужно, чтоб `dumper` по умолчанию писал в ```sys.stderr```, если на вход ```stream is None```. 
* В качестве потока для написания своих тестов для `dumper` удобно использовать [io.StringIO](https://docs.python.org/3/library/io.html#io.StringIO)
* Чтоб лучше разобраться в исключениях, что у него за аргументы и трейсбек, читайте в [exceptions](https://docs.python.org/3.6/library/exceptions.html)
* Для извлечения информации о перехваченном исключении использовать модуль [sys](https://docs.python.org/3.6/library/sys.html#sys.exc_info)
* Чтоб сдампить в dumper только исключение без трейсбека, можно воспользоваться [traceback.format_exception_only](https://docs.python.org/3/library/traceback.html#traceback.format_exception_only)
* Для создания контекстных менеджеров рекомендуем использовать модуль [contextlib](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager)
* Если будут трудности с `contextlib`, то можно создать классический [класс контекстный менеджер](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers)
переопределив ```__enter__``` и ```__exit__```
* Как связаны два способа задания контекстных менеджеров можно прочитать в [статье](http://pythonz.net/references/named/contextlib.contextmanager).
Тем не менее рекомендуем в первую очередь читать документацию.
