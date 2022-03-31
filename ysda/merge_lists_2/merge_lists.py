import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> tp.List[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    answer: tp.List[int] = []
    if len(seq) > 0:
        answer = list(seq[0])
        k = len(seq)
        for i in range(k-1):
            answer = list(heapq.merge(answer, seq[i + 1]))
        return answer
    else:
        return answer
