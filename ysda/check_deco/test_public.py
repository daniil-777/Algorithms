import pytest

from check_deco import takes


def test_example():
    @takes(int, str)
    def f(a, b):
        pass

    with pytest.raises(TypeError):
        f(1, 2)
