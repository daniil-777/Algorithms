from broken_module import force_load


def test_load_broken():
    module = force_load('auxiliary_broken')
    assert module['popper']([1, 2, 3]) == 3
