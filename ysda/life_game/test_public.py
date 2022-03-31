import pytest
from types import FunctionType

from .life_game import LifeGame


class Case:
    def __init__(self, board, expected, generation_number):
        self.board = board
        self.expected = expected
        self.generation_number = generation_number


TESTS = [
    Case(
        board=[
            [0, 2, 0],
            [0, 2, 0],
            [0, 2, 0]
        ],
        expected=[
            [0, 0, 0],
            [2, 2, 2],
            [0, 0, 0]
        ],
        generation_number=1
    ),
    Case(
        board=[
            [0, 0, 0, 0],
            [0, 3, 3, 0],
            [0, 3, 3, 0],
            [0, 1, 0, 1]
        ],
        expected=[
            [0, 0, 0, 0],
            [0, 3, 3, 0],
            [0, 3, 3, 0],
            [0, 1, 0, 1]
        ],
        generation_number=7
    )
]


@pytest.mark.parametrize("test_case", TESTS)
def test_life_game(test_case):
    game = LifeGame(test_case.board)
    generation = None
    for _ in range(test_case.generation_number):
        generation = game.get_next_generation()
    assert generation == test_case.expected


def test_methods():
    methods_names = [x for x, y in LifeGame.__dict__.items() if type(y) == FunctionType]
    private_methods = {x for x in methods_names if x.startswith('_')}
    public_methods = {x for x in methods_names if not x.startswith('_')}
    assert public_methods == {'get_next_generation'}
    assert len(private_methods - {'__init__'}) > 0
