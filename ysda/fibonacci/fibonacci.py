def get_fibonacci_value(position: int, first_value: int,
                        second_value: int) -> int:
    for _ in range(position):
        first_value, second_value = second_value, first_value+second_value
    return first_value

    """
    :param position:  Position in fibonacci sequence
    :param first_value: First value of fibonacci sequence
    :param second_value: Second value of fibonacci sequence
    :return: value of fibonacci sequence on given position
    """
