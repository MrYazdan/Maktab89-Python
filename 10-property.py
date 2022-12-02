# class Chart:
#
#     def __init__(self, x_range, y_range, z_range=None):
#         self._validate_range(x_range)
#         self._validate_range(y_range)
#
#         # if z_range:
#         #     self._validate_range(z_range)
#         #     self.z_range = z_range
#
#         self.__x_range = x_range
#         self.__y_range = y_range
#
#     @staticmethod
#     def _validate_range(_range):
#         # validation
#         assert type(_range) == tuple and \
#                len(_range) == 2 and \
#                _range[0] < _range[1] and \
#                _range[0] == 0, ValueError
#
#     # getter method
#     def get_x_range(self):
#         return self.__x_range
#
#     # setter method
#     def set_x_range(self, new_range):
#         # validation
#         self._validate_range(new_range)
#
#         # assignment
#         self.__x_range = new_range
#
#
# linear_chart = Chart((0, 10), (0, 20), (0, 90))


# print(linear_chart.get_x_range())
# linear_chart.set_x_range((0, 300))
# print(linear_chart.get_x_range())

# print(linear_chart.z_range)
# linear_chart.z_range = 10
# print(linear_chart.z_range)


# Property
from random import randint
from time import sleep


class Chart:
    def __init__(self, x_range, y_range):
        self._validate_range(x_range)
        self._validate_range(y_range)

        self.__x_range = x_range
        self.__y_range = y_range

    @staticmethod
    def _validate_range(_range):
        # validation
        assert type(_range) == tuple and \
               len(_range) == 2 and \
               _range[0] < _range[1] and \
               _range[0] == 0, ValueError

    @property  # Method (Func) => Attr
    def x_range(self):
        return self.__x_range

    @x_range.setter
    def x_range(self, new_range):
        self._validate_range(new_range)
        self.__x_range = new_range

    @property
    def y_range(self):
        return self.__y_range

    @y_range.setter
    def y_range(self, new_range):
        self._validate_range(new_range)
        self.__y_range = new_range

    @property
    def rand_number(self):
        from random import randint
        return randint(-10000000, 10000000)

    # y_range = property(fget=y_range)


linear_chart = Chart((0, 10), (0, 20))


# print(linear_chart.rand_number)
# print(linear_chart.x_range)

# linear_chart.x_range = 1000
# print(linear_chart.y_range)
#
# linear_chart.x_range = (0, 100)
# print(linear_chart.x_range)


class PieChart:
    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range

    @staticmethod
    def _validate_range(_range):
        # validation
        assert type(_range) == tuple and \
               len(_range) == 2 and \
               _range[0] < _range[1] and \
               _range[0] == 0, ValueError

    @property
    def x_range(self):
        return self.__x_range

    @x_range.setter
    def x_range(self, new_range):
        # validate
        self._validate_range(new_range)
        self.__x_range = new_range

    @property
    def y_range(self):
        return self.__y_range

    @y_range.setter
    def y_range(self, new_range):
        # validate
        self._validate_range(new_range)
        self.__y_range = new_range


# maps = PieChart((0, 1000), 0)


class Cache:
    def __init__(self):
        self.data_list = {}

    def runner(self, func, value):
        if value not in self.data_list:
            result = func(value)
            self.data_list[value] = result
            return result
        print("--- From Cached ---")
        return self.data_list[value]


from functools import cache


@cache
def f(number):
    sleep(randint(5, 10))
    return f"Number is : {number}"


cache = Cache()

while True:
    _ = int(input("> "))
    # print(cache.runner(f, _))
    print(f(_))

    print('\n', "-" * 15, '\n')
