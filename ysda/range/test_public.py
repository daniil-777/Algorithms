from range import Range


def test_basic():
    n = 0
    for i in Range(10):
        n += i
    assert n == 45


def test_repr():
    assert 'range(10, 20, 2)' == str(Range(10, 20, 2))


def test_len():
    assert 100 == len(Range(100))


def test_contains():
    assert 10 in Range(11)
    assert 10 not in Range(10)


def test_access():
    assert 2 == Range(1, 3)[1]
