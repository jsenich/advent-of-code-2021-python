from functools import wraps
from time import time


def print_time(f):
    @wraps(f)
    def wrap(*args, **kw):
        start_time = time()
        result = f(*args, **kw)
        end_time = time()
        print(f'{f.__name__}() took: {end_time-start_time:2.4f} sec')
        return result
    return wrap
