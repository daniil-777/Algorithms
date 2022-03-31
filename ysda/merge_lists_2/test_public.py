import copy
import dataclasses
import itertools
import dis

import typing as tp

import pytest


from .merge_lists import merge


@dataclasses.dataclass
class Case:
    lists: tp.Sequence[tp.Sequence[int]]
    name: str

    def __str__(self) -> str:
        return 'merge_{}'.format(self.name)


def make_test_cases() -> tp.Generator[Case, None, None]:
    for i in range(10):
        lists: tp.List[tp.List[int]] = [[] for i in range(i + 1)]

        for j in range(2000):
            basket = j % (i + 1)
            lists[basket].append(j)
        yield Case(lists=lists, name="list_" + str(i))

    yield Case(lists=[], name="list_empty")
    yield Case(lists=[[], [], []], name="list_with_empty_lists")

    for i in range(10):
        lists = [[] for i in range(i + 1)]
        for j in range(2000):
            basket = j // (2000 // (i + 1) + 1)
            lists[basket].append(j)

        yield Case(lists=lists, name="list_by_blocks_" + str(i))

    for i in range(10):
        lists = [[] for i in range(i + 1)]
        for j in range(2000):
            basket = j // (2000 // (i + 1) + 1)
            lists[basket - (basket % 2)].append(j)

        yield Case(lists=lists, name="list_by_blocks_with_gaps" + str(i))

    yield Case(lists=[[1], [1]], name="lists_with_same_elements")


def test_function_structure() -> None:
    is_used_sorted = any(i.argval == 'sorted' for i in dis.get_instructions(merge))
    assert not is_used_sorted, "You should use iteration ONLY, not manually sorting"

    is_used_build_slice = any(i.opname == 'BUILD_SLICE' for i in dis.get_instructions(merge))
    assert not is_used_build_slice, "You should use iteration ONLY, not slicing"

    is_used_heapq = any(i.argval == 'heapq' for i in dis.get_instructions(merge))
    assert is_used_heapq, "You should use heapq"


@pytest.mark.parametrize('t', list(make_test_cases()), ids=str)
def test_merge(t: Case) -> None:

    given_lists = copy.deepcopy(t.lists)
    answer = merge(given_lists)

    assert t.lists == given_lists, "You shouldn't change inputs"
    assert answer == sorted(itertools.chain(*t.lists))
