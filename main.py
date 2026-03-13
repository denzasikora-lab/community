# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import functools
import logging
import time
from typing import Callable
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'[{func.__name__}] executed in {elapsed:.4f}s')
        return result
    return wrapper


@timer
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    pass


def read_file_by_words(filename):
    with open(filename, 'r') as f:
        it = (w for line in f for w in line.split())

        while True:
            w = next(it)
            sent = yield w

            while sent is not None:
                n = int(sent)
                if n == 0:
                    sent = yield []     # чтобы после строки print(rfbw.send(0)) не было []
                    continue    # если return, то сама жизнь прервется и след print(next(rfbw)) не будут работать

                # buf = [next(it) for _ in range(n)]
                buf = []
                for _ in range(n):
                    buf.append(next(it))
                sent = yield buf


# def cache(func: Callable):
#     cached = {}
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key = str(args) + '-' + str(kwargs)
#
#         if key in cached:
#             res = cached[key]
#             logger.info(f'{func.__name__} get result {res} from cache')
#             return res
#         else:
#             res = func(*args, **kwargs)
#             cached[key] = res
#             return res
#     return wrapper


def cache(ttl: int):
    cached = {}

    def inner(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + '-' + str(kwargs)

            if key in cached and cached[key]['expired_at'] > (time.time()):
                res = cached[key]['data']
                logger.info(f'{func.__name__} get result {res} from cache')
                return res
            else:
                res = func(*args, **kwargs)
                cached[key] = {
                    'data': res,
                    'expired_at': time.time() + ttl
                }
                return res
        return wrapper
    return inner


@cache(5)
def add(a, b):
    print("cache(5)(add)(2, 3)")
    return a + b


if __name__ == '__main__':
    print_hi('PyCharm')

    print(add(2, 3))
    time.sleep(4)
    print(add(2, 3))


    # rfbw = read_file_by_words('file.txt')
    # print(next(rfbw))
    # print(next(rfbw))
    # print(rfbw.send(1))
    # print(rfbw.send(0))
    # print(rfbw.send(2))
    # print(next(rfbw))
    # print(rfbw.send(2))
    # for word in rfbw: print(word)

