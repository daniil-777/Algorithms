from .list_twist import ListTwist


def test_after_set_first():
    extended_list = ListTwist([6, 4, 5])

    extended_list.first = 8

    assert extended_list.data == [8, 4, 5]
    assert extended_list == [8, 4, 5]

    assert extended_list.reversed == [5, 4, 8]
    assert extended_list.R == [5, 4, 8]

    assert extended_list[0] == 8
    assert extended_list.first == 8
    assert extended_list.F == 8

    assert extended_list[-1] == 5
    assert extended_list.last == 5
    assert extended_list.L == 5

    assert len(extended_list) == 3
    assert extended_list.size == 3
    assert extended_list.S == 3
