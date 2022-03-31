## Виртуальная машина

### Введение

Выполнение кода в [интерпретаторе](https://ru.wikipedia.org/wiki/Интерпретатор) CPython происходит в две фазы: сначала синтаксис 
языка компилируется в более простой, байткод, а после этот байткод 
выполняется в виртуальной машине.

Интерпретатор питона - это виртуальная машина, или если более точно, стековая
 машина. Стековая машина оперирует несколькими стеками, а команды байткода задают какие-то операции над этими стеками. 

Процесс можно провести и собственноручно. Для этого надо последовательно вызвать в
интерпретаторе функции ```compile``` и ```exec/eval```. 
Например,
```ipython
In [1]: a = """
   ...: for i in range(3):
   ...:     print(i)
   ...: """
In [2]: eval(compile(a, '<stdin>', 'exec'), {}, {})
0
1
2
```

Чтоб понять, как устроен байткод, можно вызвать функцию dis.dis.

```ipython
In [1]: import dis
In [2]: dis.dis("print('hello')")
  1           0 LOAD_NAME                0 (print)
              2 LOAD_CONST               0 ('hello')
              4 CALL_FUNCTION            1
              6 RETURN_VALUE
```

### Пример

Давайте рассмотрим такое выражение:
```python
print(1 + 2 * 3)
```

Его байткод можно достать например так:
```python
code = list(compile('print(1 + 2 * 3)', '<test>', 'exec').co_code)
```
Результат - список операций, которые надо выполнять последовательно
```python
[101, 0, 100, 5, 131, 1, 1, 0, 100, 3, 83, 0]

```
С тем какая цифра какую операцию задает – поможет dis
```ipython
In [6]: dis.opname[101]
Out[6]: 'LOAD_NAME'
```

Наглядно увидеть весь байткод функции можно через dis.dis
```ipython
In [13]: codeobj = compile('print(1 + 2 * 3)', '<test>', 'exec')
In [14]: codeobj.co_consts
Out[14]: (1, 2, 3, None, 6, 7)
In [15]: dis.dis(codeobj)
  1           0 LOAD_NAME                0 (print)
              2 LOAD_CONST               5 (7)
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               3 (None)
             10 RETURN_VALUE
```
Как уже говорилось выше, инструкции байткода взаимодействуют со стеком.

LOAD_NAME - загружает функцию print на вершину стека.

LOAD_CONST кладёт сверху константу, 5ю в списке констант со значением 7.

CALL_FUNCTION вызывает функцию с какими-то аргументами (в данном случае print с одним аргументом).

С тем, как устроены более сложные структуры байткода вам предлагается разобраться самим, поисследовав тривиальные примеры.

Также очень удобно достать список всех инструкций, чтоб не возиться с оффсетами:
```ipython
In [16]: list(dis.get_instructions(codeobj))
Out[16]:
[Instruction(opname='LOAD_NAME', opcode=101, arg=0, argval='print', argrepr='print', offset=0, starts_line=1, is_jump_target=False),
 Instruction(opname='LOAD_CONST', opcode=100, arg=5, argval=7, argrepr='7', offset=2, starts_line=None, is_jump_target=False),
 Instruction(opname='CALL_FUNCTION', opcode=131, arg=1, argval=1, argrepr='', offset=4, starts_line=None, is_jump_target=False),
 Instruction(opname='POP_TOP', opcode=1, arg=None, argval=None, argrepr='', offset=6, starts_line=None, is_jump_target=False),
 Instruction(opname='LOAD_CONST', opcode=100, arg=3, argval=None, argrepr='None', offset=8, starts_line=None, is_jump_target=False),
 Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=10, starts_line=None, is_jump_target=False)]

```
### Задание

В данном задании вам нужно написать интерпретатор байткода питона на питоне.
Для этого в файле ```vm.py``` нужно реализовать метод ```run```.

Комментарии:
* Задание намеренно не содержит полной спецификации работы виртуальной ма-
шины. Разобраться в том как работают, например, функции – ваша задача, не
просите семинаристов вам это объяснить.
* Не стесняйтесь гуглить, читать и обсуждать между собой какие-то вопросы
которые вам непонятны. В интернете много детальных разборов этой темы. (Но
помните, что заимствование кода, как из сети, так и у однокурсников карается
полным незачетом задания всем причастным).
* Часть тем, затронутых в условии и необходимых для выполнения задания (например модули и импорт), 
пока не рассказана на лекциях, но будет затронута
на одной из ближайших.

### Оценка

Частичное решение тоже является решением и будет оценено. 
Засчитывается последнее отправленное решение. 
Поэтому если у вас было 300 баллов за задачу, а вы засабмитили после этого на 200, то в гуглдок пойдет 200.

Результирующий балл - сумма баллов по всем тестам.

Тесты поделены на 4 уровня. Уровень теста - максимальный уровень операции, который в нем встречается.

* 1 уровень - базовый. Дает 50% баллов (175 баллов)
* 2 уровень - средний. Дает 80% баллов (175 +105 баллов)
* 3 уровень - высокий. Дает 100% баллов (175 +105 +70 баллов)
* 4 уровень - супермэн. Дает 100% баллов + 50 баллов бонуса (175 +105 +70 + 50)

Стоимость теста = Баллы за уровень / Число тестов на уровне

Уровни операций - в файле ```vm_scorer.py```

### Как протестировать

```bash
ilariia@ilariia-osx1:~/jhilary/vm(master)$ ~/.pyenv/versions/3.6.3/bin/pytest test_public.py
======================================================= test session starts ========================================================
platform darwin -- Python 3.6.3, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
rootdir: /Users/ilariia/jhilary/vm, inifile:
plugins: requests-mock-1.5.2
collected 10 items

test_public.py ..........

==================================================== 10 passed in 0.09 seconds =====================================================
ilariia@ilariia-osx1:~/jhilary/vm(master)$
```

Нужно добавлять свои тесты в ```cases.py```, начиная с самых простых операций.

Есть еще очень полезный тест, который показывает насколько хорошо вы покрыли все операции тестами.
```
ilariia@ilariia-osx1:~/jhilary/vm(master)$ ~/.pyenv/versions/3.6.3/bin/pytest test_public.py::test_stat -s
======================================================= test session starts ========================================================
platform darwin -- Python 3.6.3, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
rootdir: /Users/ilariia/jhilary/vm, inifile:
plugins: requests-mock-1.5.2
collected 1 item

test_public.py
Test operations distribution:
	BEFORE_ASYNC_WITH: 0
    ...
	YIELD_VALUE: 0
Tests levels distribution:
	0: 0
	1: 1
	2: 1
	3: 1
	4: 1
Operations coverage:
	22/118
Operations by levels coverage:
	0: 0/2
	1: 15/65
	2: 4/28
	3: 1/12
	4: 2/11
Maximum score on tests set:
	400.0
```

### Как начать и что делать

В таком порядке стоит разбирать и реализовывать механизмы интерпретатора, 
каждое следующее реализовать сложнее чем предыдущее:
* Функция **print** и арифметика, переменные, арифметические и логические
типы
* Условия и циклы
* Строки, форматирование
* Списки, словари, кортежи, генераторы списков, распаковка, слайсы
* Функции и фреймы(!), замыкания, декораторы
* Классы

### Запрещено

Нельзя использовать в реализации **exec**, **eval**, **FunctionType**.
Также нельзя писать реализацию функций подменой __code__:
```
        def f():
            pass
        f.__code__ = code
        f()
```
Это обусловлено тем, что таким образом вы вызываете интерпретатор питона, а не пишете свой. 
А задание именно в том, чтоб написать его самим.


### Очень полезные ссылки

* Документация к dis: https://docs.python.org/3/library/dis.html 
Там описаны все существующие операции байткода
* Академический проект интерпретатора для PY27 и PY33, снабженный множеством комментариев, 
но не лишенный проблем: https://github.com/nedbat/byterun
Его детальное обсуждение в блоге:
http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
* Исходный код родного интерпретатора PY36 - поможет разобраться с тонкостями 
https://github.com/python/cpython/blob/3.6/Python/ceval.c
* Еще одна вводная статья - http://www.goldsborough.me/python/low-level/2016/10/04/00-31-30-disassembling_python_bytecode/
* https://habrahabr.ru/company/buruki/blog/189972
* http://akaptur.com/blog/2013/11/17/introduction-to-the-python-interpreter-3
* https://www.quora.com/What-is-Python-byte-code
* http://security.coverity.com/blog/2014/Nov/understanding-python-bytecode.html
* http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python
* http://multigrad.blogspot.ru/2014/06/fun-with-python-bytecode.html
