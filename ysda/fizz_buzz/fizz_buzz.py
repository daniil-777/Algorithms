from typing import List, TypeVar

FizzBuzzType = TypeVar('FizzBuzzType', int, str)


def get_fizz_buzz(n: int) -> List[FizzBuzzType]:
    list = []
    for i in range(1, n+1):
        if i % 15 == 0:
            list.append("Fizz Buzz")
        elif(i % 5 == 0):
            list.append("Buzz")
        elif(i % 3 == 0):
            list.append("Fizz")
        else:
            list.append(i)
    return list
    """
    :param n: size of sequence
    :return: list of values. If value divided by 3 - "Fizz",
    if value divided by 5 - "Buzz", if value divided by 15 -
            "Fizz Buzz", else - value.
    """
