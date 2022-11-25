class Mother:pass


class Father:
    def hi(self):
        print("Father: Hi")


class Child(Mother, Father):
    def hi(self):
        super().hi()
        print("Child: Hi")


c1 = Child()
c1.hi()
print(Child.mro())

