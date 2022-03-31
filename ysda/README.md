# Инструкция по настройке окружения и сдаче заданий

## Настройка окружения

 1. Вам надо зарегистрироваться на [py.manytask.org](http://py.manytask.org/).
<div>
<img src="/.img/login.png"  alt="login" width="500">
<img src="/.img/instruction.png"  alt="login" width="500">
</div>

 2. Надо зайти в свой репозиторий на https://gitlab.manytask.org и добавить публичный ssh-ключ в настройках профиля.
 Для того, чтобы сгенерировать ключ, используйте `ssh-keygen`

 3. Склонируйте и настройте репозиторий
 ```bash
 $ git clone https://gitlab.com/Gezort/shad-py $USERNAME
 $ cd $USERNAME
 $ git config --global user.name $USERNAME
 $ git config --global user.email $EMAIL
 $ git remote add student git@gitlab.manytask.org:python-autumn-2018/$USERNAME.git
 ```

 4. Установите питоновские пакеты
 
 Необходимые версии:

 ```bash
 $ python --version
 Python 3.6.3
 $ pytest --version
 This is pytest version 3.2.3, ...
 $ pycodestyle --version
 2.4.0
 ```
 
 **Если не хотите ходить по граблям, проверьте, что версии у вас совпадают**

 Как установить:
 ```
 $ pip3 install --upgrade pycodestyle==2.4.0 pytest==3.2.3
 ```

## Сдача заданий

Для получения новых заданий надо делать `git pull`. Для локального тестирования кода вам понадобится библиотека `pytest`. Ее можно поставить через `pip`


Код относящийся к отдельной задаче находится в отдельной директории
(`hello_world` и т.д.). Там же находится условие задачи
(`hello_world/README.md`).

```bash
# Переходим в задачу
$ cd hello_world

# Пишем код в файле hello_world.py, реализовывая заданный интерфейс

# Запускаем юниттесты
hello_world$ pytest .

# Проверяем код-стайл
hello_world$ pycodestyle .

# Отправляем задачу в систему
hello_world$ python3 ../submit.py

# У скрипта есть флаг -v - если что-то не работает, попробуйте починить сами:w
```
Скрипт создаст новый коммит и запушит его в репозиторий. Вы
сможете наблюдать за результатами тестирования на странице `CI/CD -> Pipelines` в своём репозитории.

Там можно увидеть статусы посылок и результаты тестирования.

**Если submit не заработал:** внимательно изучите [памятку про коммон проблемы с ssh](https://gitlab.com/Gezort/shad-py/wikis/SSH-common-problems)
