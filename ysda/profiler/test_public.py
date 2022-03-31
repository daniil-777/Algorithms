from datetime import datetime

from profiler import profiler


@profiler
def ackerman(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackerman(m - 1, 1)
    if m > 0 and n > 0:
        return ackerman(m - 1, ackerman(m, n - 1))


def test_example():
    start = datetime.now()
    result = ackerman(3, 2)
    delta = datetime.now() - start

    assert ackerman.calls == 541
    assert ackerman.last_time_taken <= delta.total_seconds()
    assert result == 29
