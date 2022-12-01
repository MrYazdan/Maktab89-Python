from abc import ABC, abstractmethod


# class BaseBook(ABC):
#
#     @abstractmethod
#     def read(self):
#         raise NotImplementedError
#
#
# class Book(BaseBook):
#
#     def __init__(self, name) -> None:
#         self.name = name
#
#     def read(self):
#         print("Read !")
#
#
# physic = Book('Physic from hard way !')
# print(isinstance(physic, BaseBook))

# base_physic = BaseBook()

class BaseGun(ABC):
    attachments = []

    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def reload(self):
        pass


class BaseSniper(BaseGun):
    def fire(self):
        pass

    def reload(self):
        pass


class Sniper(BaseSniper):
    pass


class AWP(Sniper):
    def fire(self):
        pass

    def reload(self):
        pass


awp = AWP()
