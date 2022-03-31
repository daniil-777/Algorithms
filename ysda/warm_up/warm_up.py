from typing import List
from typing import Iterator
from typing import TypeVar
from typing import Dict

T = TypeVar('T')


def transpose(matrix: List[List]) -> List[List]:
    """
    :param matrix: rectangular matrix
    :return: transposed matrix
    """
    pass


def uniq(sequence: List[T]) -> Iterator[T]:
    """
    :param sequence: arbitrary sequence of comparable elements
    :return: generator of elements of `sequence` in
    the same order without duplicates
    """
    pass


def dict_merge(*dicts: Dict) -> Dict:
    """
    :param *dicts: flat dictionaries to be merged
    :return: merged dictionary
    """
    pass


def product(lhs: List[int], rhs: List[int]):
    """
    :param rhs: first factor
    :param lhs: second factor
    :return: scalar product
    """
    pass
