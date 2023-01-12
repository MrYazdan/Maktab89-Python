# numbers = [1, 2, 3, 4, 6, 7, 8, 9, 0, 5]

# for number in numbers:
#     print(number)


# def iterator(iterable):
#     if len(iterable) > 1:
#         print(iterable[0])
#         return iterator(iterable[1:])
#     print(iterable[0])
#
#
# iterator(numbers)

# it = iter(numbers)

# def next(iterable):
#     return iterable.pop(0)
#
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

class Numbers:
    def __init__(self, data):
        self.data = data

    # def __getitem__(self, item):
    #     return self.data[item]

    def __iter__(self):
        for number in self.data:
            print("Iter :", number)
            yield number

    def __next__(self):
        print("Next called")


numbers = Numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(numbers[0])

# for n in numbers:
#     print(n)

it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print(next(it))
