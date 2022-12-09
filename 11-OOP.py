import shelve
from abc import ABC, abstractmethod
from random import randint


class Machine:
    __ids = []

    def __init__(self, name):
        self.name = name
        self.id = self.id_generator()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        """
            validation
        """
        self._name = value

    @classmethod
    def id_generator(cls):
        if (generated_id := randint(11111, 99999)) not in cls.__ids:
            cls.__ids.append(generated_id)
            return generated_id
        return cls.id_generator()

    @staticmethod
    def is_machine(self, machine_id):
        return 11111 <= machine_id <= 99999


# pride = Machine('Pride')
# print(pride.id)
#
# print(Machine.is_machine(77651))
# print(pride.id_generator())


class Validators:

    @classmethod
    def mail(cls, mail):
        return True


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y


class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x, x)

    def area(self):
        print("Area method in Square ... ")
        return super().area()


class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.x


# s1 = Square(4)
# print(s1.perimeter())

# c1 = Cube(4)
# print(c1.surface_area())

class Odd:
    def __new__(cls, number):
        if number % 2 != 0:
            return super().__new__(cls)
        raise PermissionError

    def __init__(self, number):
        self.number = number


# n1 = Odd(3)
# # n1 = Odd(4)
# print(n1.number)


class BaseTurboMotors(ABC):

    @abstractmethod
    def nitro(self):
        raise NotImplementedError


class BenzMotorMixins:
    diaphragm = 4.8
    fuel_type = "gasoline"

    @staticmethod
    def voice():
        print("'''''''''''''''''''''''''''")


class BenzMotor(BaseTurboMotors, BenzMotorMixins):
    def __init__(self, name, top_speed):
        self.name = name
        self.top_speed = top_speed

    def nitro(self):
        print("Nitro Called !")


# z473 = BenzMotor("Flagship", 400)

class Car:
    cars = []

    def __init__(self, name):
        self.name = name
        self.__class__.cars.append(self)

    def __repr__(self):
        return f"< {self.name} >"


db = shelve.open("cars.db", "c")

if not db.get('cars', None):
    db['cars'] = []

print("Cars in db :", db['cars'])

while True:
    cmd = int(input("1. new car\n2. list car\n\n> "))

    if cmd == 1:
        print("New car --------------")
        car_name = input("> ")
        Car(car_name)
        db['cars'] = Car.cars
        input("Created ! ...")

    elif cmd == 2:
        print(db['cars'])
        input()

    else:
        break

db.close()
