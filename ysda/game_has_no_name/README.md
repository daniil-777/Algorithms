## ИГРА БЕЗ ИМЕНИ

### Пререквизиты

Python версии 3.6.3. Pytest версии 3.2.3.

### Условие

Мы хотим сыграть с вами в игру. 
Игра представляет из себя класс на питоне у которого есть некоторое (большое)
 количество методов, которые надо позвать в правильном порядке. 
Каждый из этих методов принимает единственный параметр – 
объект типа Player, которому она скажет какой метод надо звать следующим.
Тонкость состоит в том, что игра сама решает как именно обращаться к игроку, 
и каждый раз при обращении говорит ему не только метод, к которому надо обратиться к ней, 
но и метод, который она позовет у игрока в следующий раз, чтобы сказать ему новые имена. 
Более того, игра не любит жуликов, и игроку разрешено иметь только один 
правильный метод для приема новых имен, если в нём будут старые методы - 
ей это не понравится.
Игра заканчивается по желанию игры. Она выбросит правильное исключение, 
и мы его обработаем зачтя вам задачу.
Для начала игры надо позвать у обьекта класса Game метод start, 
которому надо передать на вход объект класса Player, 
у которого должен быть метод ready. 
Вызывая этот метод игра передаст в него новые названия методов, 
которые заменят (start, ready) в следующей итерации.
 
### Замечание

* Не мудрите, решение занимает 25-30 строк.
* Игра происходит блоками, а не рекурсивно:
  - player.play() -> game.start(player) -> player.ready('start2', 'ready2')
  - player.play() -> game.start2(player) -> player.ready2('start3', 'ready3')
  - ...

### Пример запуска тестов

Если хотите сами потестировать игру, то вам нужно самим ее реализовать в ```test_public.py```.
Тогда тесты будут запускаться так:
```bash
ilariia@ilariia-osx1:~/shad-py/game_has_no_name(master)$ ~/.pyenv/versions/3.6.3/bin/pytest .
```