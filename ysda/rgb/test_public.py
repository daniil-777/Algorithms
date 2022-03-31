from rgb import parse_color


def test_hex():
    assert parse_color('#AAaaaa') == [170, 170, 170]


def test_trivial():
    assert parse_color('rgb(1, 2, 3)') == [1, 2, 3]


def test_none():
    assert parse_color('#gggggg') is None


def test_mess():
    assert parse_color('brg(70, 71, 72)') == [71, 72, 70]


def test_spaces():
    assert parse_color('rgb(   255, 255,    255 )') == [255, 255, 255]
