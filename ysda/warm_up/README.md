## Разминка


### Условие

В этом задании вам нужно реализовать 4 простые функции. Рекомендуем пользоваться модулями
itertools и operator.

## 1. Транспонирование

Нужно реализовать функцию ```transpose``` которая транспонирует матрицу. На вход функции 
подается матрица в виде списка строк, строки -- это непустые списки одинаковой длины состоящие 
из произвольных питоновских объектов. Постарайтесь написать функцию-однострочник.

На выходе список списков, представляющий транспонированную матрицу.

#### Пример
```
>>> transpose([[1, 2], [3, 4], [5, 6]])
[[1, 3, 5], [2, 4, 6]]
```

## 2. Удаление дубликатов

Нужно реализовать функцию-генератор ```uniq``` которая получает на вход итератор и 
возвращает элементы в том же порядке, убирая дубликаты

#### Пример
```
>>> list(uniq([1, 2, 3, 3, 1, 7]))
[1, 2, 3, 7]
```

## 3. Объединение словарей.

Нужно реализовать функцию ```dict_merge``` которая принимает на вход произвольное количество
словарей и возвращает результат их объединения. Словари имеют плоскую структуру. Значения по
ключам в словарях перезатирают значения из по тем же самым ключам из словарей упомянутых 
раньше в списке аргументов. Постарайтесь написать функцию-однострочник.

#### Пример
```
>>> dict_merge({1:2}, {2: 2}, {1: 1})
{1: 1, 2: 2}
```

## 4. Скалярное произведение

Нужно реализовать функцию ```product``` вычисляющую скалярное произведение двух векторов.
Векторы - одинаковой длины и представлены списками чисел. Постарайтесь написать 
функцию-однострочник.

#### Пример
```
>>> product([1, 2, 3], [4, 5, 6])
32
```