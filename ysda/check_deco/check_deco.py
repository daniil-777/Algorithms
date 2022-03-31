import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def in_wrapper(*args, **kwargs):
            for arg, type in zip(args, types):
                if not isinstance(arg, type):
                    raise TypeError()
            return func(*args, **kwargs)
        return in_wrapper
    return decorator
