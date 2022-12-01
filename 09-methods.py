class Car:
    cars = []

    def __init__(self, name, color):
        self.name = name
        self.color = color

        # ?!#
        # self.cars.append(self)
        #
        # # 1:
        # Car.cars.append(self)
        #
        # # 2:
        # Car == self.__class__
        self.__class__.cars.append(self)

    def __repr__(self):
        return " | " + self.name + " - " + self.color + " | "

    def printer(self):
        print(self.name)

    # def print_cars(self):
    #     self.__class__.cars
    @classmethod
    def print_cars(cls):
        print(cls.cars)


pride = Car('pride', 'white')
tiba = Car('tiba', 'silver')
p206 = Car('206', 'red')

# Car.printer()  # instance method
Car.print_cars()  # class method

print([car for car in Car.cars])
