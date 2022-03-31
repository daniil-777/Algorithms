def get_seconds_diff(hours_1: int, minutes_1: int, seconds_1: int,
                     hours_2: int, minutes_2: int, seconds_2: int) -> int:
    """
    :param hours_1: hours of the first datetime
    :param minutes_1: minutes of the first datetime
    :param seconds_1: seconds of the first datetime
    :param hours_2: hours of the second datetime
    :param minutes_2: minutes of the second datetime
    :param seconds_2: seconds of the second datetime
    :return: diff between second time and first time
             with guarantee that second no less then first
    """
    answer = 3600 * (hours_2 - hours_1) + 60 * (minutes_2 - minutes_1) + seconds_2 - seconds_1
    return answer
