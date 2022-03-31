import time
import functools


def profiler(func):
    depth = 0
    recursion = []

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        nonlocal recursion

        if not recursion:
            depth = 0
        depth += 1

        wrapper.calls = depth
        recursion.append(0)
        start = time.time()
        new_func = func(*args, **kwargs)
        recursion.pop()
        wrapper.last_time_taken = time.time() - start
        return new_func

    return wrapper
