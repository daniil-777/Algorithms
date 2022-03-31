## STRINGS

### Пререквизиты

Python версии 3.6.3. Pytest версии 3.2.3.

### Условие

Есть в Unix полезная утилита ```strings``` для поиска текстовых (printable) строк в бинарных данных. 
Бесконечно полезная вещь, например, при анализе объектных файлов. Можете его натравить на наш бинарный файл так:
```bash
ilariia@ilariia-osx1:~/shad-py/strings/resources(master)$ strings small_dump.bin
Hello scoring server!`
Some noise 42232U55`
Hello you too`
What is Petr score?`
Yet another noise 2342342D4e45
Thank you scoring server! Bye-bye!`
Bye-bye!
```

Вам нужно в файле ```strings.py``` реализовать два интерфейса:
* ```strings```, который генерирует из файла все стринги
* ```strings_generator```, который генерирует из бинарного потока все строки

Параметр ```min_string_length``` указывает минимальный размер строки, которая будет определяться как текстовая.

Для утилиты ```strings``` этот параметр аналогичен параметру `-n`:
```bash
ilariia@ilariia-osx1:~/shad-py/strings/resources(master)$ strings small_dump.bin -n 30
Yet another noise 2342342D4e45
Thank you scoring server! Bye-bye!`
```

### Замечание

* Текстовыми считаются символы из набора [```string.printable```](https://docs.python.org/3/library/string.html#string.printable)
* Учтите, что файл может не влезать в память. Гарантируется, что все текстовые строки достаточно маленькие, и в память влезают.
* Стоит почитать что такое [BinaryIO](https://docs.python.org/3/library/io.html#binary-i-o) и подробнее про интерфейс в [BufferedIOBase](https://docs.python.org/3/library/io.html#io.BufferedIOBase)