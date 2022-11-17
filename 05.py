from os import name as os_name, system as terminal


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


# 10 / 0 # ZeroDivisionError
# float('salam') # ValueError
# '23' + 23 # TypeError
# print(my_variable)
# print(my_arg='my_value')
# from yazdan import name
# from time import salam

# while True:
# try:
#     number = int(input("Please enter your number : "))
# except ValueError:
#     print("Invalid input !")
#     continue
#
# if number % 2 != 0:
#     print('Thanks !')
# else:
#     input("Error !!!\n")

# w => write
# r => read
# rb, wb,


# write, read =>
# db = open("phonebooks.txt", "a+")


def register_phone_number():
    clear()
    print("------ Register ------")
    phone_number = input("Enter phone number [valid phone number = 09123334444] : ")

    # len = 11
    # phone_number[:2] = '09'

    assert len(phone_number) == 11 and phone_number[:2] == '09', "phone number is not valid !"

    fullname = input("Enter phone name : ")

    # str , numeric

    assert not fullname.isnumeric(), "fullname not valid !"

    with open("phonebooks.txt", "a+") as db:
        db.write(f"{fullname}::{phone_number}\n")

    input("Your number saved ! \n\nPress enter to back main ... ")


menu_items = [
    'register phone number',
    'list phone numbers',
    'search phone numbers',
    'about',
    'exit',
]

line = "-" * 22

while True:
    clear()
    print("-------- Menu --------")

    for index, value in enumerate(menu_items):
        print(index + 1, value)
    print(line)

    try:
        user_number = int(input("> "))
        func = menu_items[user_number - 1]
        func = func.replace(" ", "_")

        eval(f"{func}()")

    except (ValueError, IndexError):
        input("Error !!! \n\nPress enter to back main ... ")

    except AssertionError as msg:
        input(msg)
        eval(f"{func}()")

# db.close()
