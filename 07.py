# Snake case
def say_hello(name):
    print(f"Hello {name}")


# Pascal case
# class Human:
#     age = None
#     name = None
#
#
# reza = Human()
# reza.name = "reza"
# reza.age = 23
#
# print(reza, reza.name, reza.age, sep="\n")

class Human:
    phone = "09123334444"
    name = "alireza"

    def __init__(self, name_str, age_number):
        self.name = name_str
        self.age = age_number

    def hi(self):
        print(f"Hi from {self.name} to you !")


reza = Human("reza", 23)


# print(reza.name, reza.age, sep="\n")
# reza.hi()

# Human.phone = "09334445555"

# print(reza.name)
# print(reza.phone)

# inheritance
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Flying !")


class Sparrow(Bird):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


gonjeshk = Sparrow("gonjeshk", "Yellow")
gonjeshk.fly()
print(gonjeshk.name)
print(gonjeshk.color)
