import pytest

from .game_has_no_name import play, Player

MAX_DEPTH = 65839


class WinException(Exception):
    def __init__(self, value):
        self.prise = value
        super().__init__()


class LooseException(Exception):
    pass


class Game(object):
    def start(self, player: Player):
        pass


def test_player():
    with pytest.raises(WinException):
        g = Game()
        play(g)
