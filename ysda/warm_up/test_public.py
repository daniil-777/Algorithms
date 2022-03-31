import pytest
from collections import OrderedDict


from .warm_up import transpose
from .warm_up import uniq
from .warm_up import dict_merge
from .warm_up import product


TRANSPOSE_TEST_CASES = OrderedDict([
    (
        'transpose_test_case_0',
        (
            [[1, 2], [3, 4], [5, 6]],
            [[1, 3, 5], [2, 4, 6]]
        )
    )
])


@pytest.mark.parametrize(
    'matrix,expected',
    TRANSPOSE_TEST_CASES.values(),
    ids=list(TRANSPOSE_TEST_CASES.keys())
)
def test_transpose(matrix, expected):
    assert transpose(matrix) == expected


UNIQ_TEST_CASES = OrderedDict([
    (
        'uniq_test_case_0',
        (
            [1, 2, 3, 3, 1, 7],
            [1, 2, 3, 7]
        )
    )
])


@pytest.mark.parametrize(
    'sequence,expected',
    UNIQ_TEST_CASES.values(),
    ids=list(UNIQ_TEST_CASES.keys())
)
def test_uniq(sequence, expected):
    assert list(uniq(sequence)) == expected


DICT_MERGE_TEST_CASES = OrderedDict([
    (
        'dict_merge_test_case_0',
        (
            [{1: 2}, {2: 2}, {1: 1}],
            {1: 1, 2: 2}
        )
    )
])


@pytest.mark.parametrize(
    'dicts,expected',
    DICT_MERGE_TEST_CASES.values(),
    ids=list(DICT_MERGE_TEST_CASES.keys())
)
def test_dict_merge(dicts, expected):
    assert dict_merge(*dicts) == expected


PRODUCT_TEST_CASES = OrderedDict([
    (
        'product_test_case_0',
        (
            [1, 2, 3],
            [4, 5, 6],
            32
        )
    )
])


@pytest.mark.parametrize(
    'lhs,rhs,expected',
    PRODUCT_TEST_CASES.values(),
    ids=list(PRODUCT_TEST_CASES.keys())
)
def test_product(lhs, rhs, expected):
    assert product(lhs, rhs) == expected
