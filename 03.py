age = 21
name = "Akbar"
phone_number = "09123456789"

# name, age, phone
# print(name, age, phone_number)
# printed_text = name + str(age)
# printed_text = f"name is : {name=}\nage is : {age * 2}"
normal_text = "name is {}\nAge is {}".format(name, age)
old_text = "hello %s, age is %d" % (name, age)


# print(normal_text)
# print(printed_text)
# print(old_text)

# range function :
# range(start, end, step)


# prop
# 1. part
# 2. clean

# Reuse
def say_hi():
    print("Salam refigh !")


def power_two():
    return 2 ** 2


# print(say_hi())
# print(power_two())


# def power(number=2, power_number=2):
#     return number ** power_number
#
#
# print(power(2))
# print(power(2, 3))
# print(power())


def printer(text_list, end="\t"):
    for text in text_list:
        print(text, end=end)


texts = [
    "this is test text.",
    "i am reza !",
    "how are you ?"
]

# printer(texts, end=" -- ")

# range => stop required!

# print(list(range(10)))  # range(stop=10)
# print(list(range(10)))
# print(list(range(10)))
# print(list(range(stop=50, start=30)))

# print(type("reza"))  # str
# print(type(12.2))  # float
# print(type([1, 2, 3]))  # list


# def test(value):
#     # if type(value) == str:
#     if isinstance(value, str):
#         print(value + " + develop by amin")
#     # elif isinstance(value, (float, int)):
#     elif type(value) == int or float:
#         print(value + 1)


# test("hello")
# test(12.3)
# test(12)

text = "this is test text !"

# value = 12

# print(len(text))
# print(len(value))
# print(range(len(text)))
#
# print(abs(True))

number = 12.395995353534
# number = str(number).split('.')
# number = f"{number[0]}.{number[1][:2]}"

# print(f"{number:1f}")

numbers = [10, 20, 30, 23, 45, 243, 23, 1, 23]


# max , min , sum
# sum(numbers)
# print(min(numbers))
# print(max(numbers))

# print(sorted(numbers))

# print(numbers)
# print(numbers.sort())
# print(numbers)

# print(round())



