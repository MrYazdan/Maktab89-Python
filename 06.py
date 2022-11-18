# import time
# from time import sleep

# print("before sleep !")

# time.sleep(5)
# sleep(5)

# print("after sleep !")

from time import time, sleep


# start_time = time()
#
# sleep(4)
#
# end_time = time()
# print(end_time-start_time)


def timeit(func):
    # print("Before create")

    def wrapper(time_second):
        start_time = time()

        # print("Before mount")
        res = max(func(time_second))
        # print("After mount | Mounted")

        end_time = time()
        print(round(end_time - start_time, 4))

        return res

    # print("After create | Created")
    return wrapper


# @timeit
# def worker(time_second: int = 2):
#     sleep(time_second)


# worker(20)


# def my_func(n):
#     return list(range(1, n))


# result = worker(2)
# print(result)

# functions = [
#     my_func, worker
# ]
#

# functions[0 => my_func
# my_func => my_func(20)
# my_func(20)[5] => 6
# print(functions[0](20)[5])

# print(my_func)

# @timeit
# def my_evens(number):
# _list = []
# for i in range(number):
#     if i % 2 == 0:
#         _list.append(i)
# return [i for i in range(number) if i % 2 == 0]
# return (i for i in range(number) if i % 2 == 0)


# print(my_evens(500000000))  # 5.8 s
import sys

s = time()

# 203199480
# evens = [i for i in range(50000000) if i % 2 == 0]

def evens(number):
    for i in range(number):
        if i % 2 == 0:
            yield i


# 104
# evens = (i for i in range(50000000) if i % 2 == 0)


print("Size of evens :", sys.getsizeof(evens))

# count = 0
# for i in evens:
#     count += 1

print(round(time() - s))
