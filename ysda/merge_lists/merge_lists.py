import typing as tp


def merge_iterative(lst_a: tp.List[int], lst_b: tp.List[int]) -> tp.List[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    n1 = len(lst_a)
    n2 = len(lst_b)
    arr3 = [0] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    # Traverse both array
    while i < n1 and j < n2:
        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if lst_a[i] < lst_b[j]:
            arr3[k] = lst_a[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = lst_b[j]
            k = k + 1
            j = j + 1
    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = lst_a[i]
        k = k + 1
        i = i + 1
    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = lst_b[j]
        k = k + 1
        j = j + 1
    return arr3


def merge_sorted(lst_a: tp.List[int], lst_b: tp.List[int]) -> tp.List[int]:
    """
    Merge two sorted lists in one sorted list ising `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    res = sorted(lst_a + lst_b)
    return res
