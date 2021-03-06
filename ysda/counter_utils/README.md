# Утилитa __wc__

Ваша задача — реализовать аналог консольной утилиты __wc__ на python.
Программа должна уметь принимать следующие ключи:
* _-m_, печатает число символов;
* _-l_, печатает число строк;
* _-L_, печатает длину самой длинной строки; </li>
* _-w_, печатает количество слов;

Обратите внимание, что ключей может быть несколько и всегда указан хотя бы один ключ.
Данные выводятся в строго определенном порядке:
число строк, число слов, число символов, максимальная длина строки, при чем все числа
пишутся в одну строку, через пробел.

PS: Согласно документации __wc__: _A line is deﬁned as a string of characters delimited by a <newline>
character. A word is deﬁned as a string of characters delimited by white space characters_.
Важно правильно учесть последний перенос строки.
      
## Формат ввода
Ваше решение будет запущено с некоторым набором указанных ключей. Они указаны в первой строке входного файла.
Далее, начиная со второй строки, дан текстовый файл, состоящий из нескольких строк.
Число строк может меняться от 0 до 100. 

## Формат вывода
Вам необходимо вывести результат работы __wc__ с указанными в первой строке входного файла ключами на тексте,
начинающемся со второй строки.

### Пример 1
```
-m
  there is one
    more
example for
 problem
```
Ответ:
`45`

### Пример 2
```
-l
  there is one
    more
example for
 problem
```
Ответ:
`4`

### Пример 3
```
-L
  there is one
    more
example for
 problem
```
Ответ:
`14`

### Пример 4
```
-w
  there is one
    more
example for
 problem
```
Ответ:
`7`

### Пример 5

```
-m -l -L -w
  there is one
    more
example for
 problem
```
Ответ:
`4 7 45 14`

## Примечания
Естественно, пользоваться консольной утилитой __wc__ в этой задаче запрещено!
Можно посмотреть в сторону [argparse](https://docs.python.org/3/library/argparse.html)
или [click](http://click.pocoo.org/5/). Будет только в плюс, если Вы с ними разберетесь!
