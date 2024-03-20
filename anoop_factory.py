# from abc import ABCMeta, abstractmethod
#
#
# class IProduct(metaclass=ABCMeta):
#     @staticmethod
#     @abstractmethod
#     def create_object():
#         """ An abstract interface method """
#
#
# class ConcreteProductA(IProduct):
#     """ A concrete class that implements the IProduct interface """
#
#     def __init__(self):
#         self.name = "ConcreteProductA"
#
#
#     def create_object(self):
#         return self
#
#
# class ConcreteProductB(IProduct):
#     """ A concrete class that implements the IProduct interface """
#
#     def __init__(self):
#         self.name = "ConcreteProductB"
#
#     def create_object(self):
#         return self
#
#
# class ConcreteProductC(IProduct):
#     """ A concrete class that implements the IProduct interface """
#
#     def __init__(self):
#         self.name = "ConcreteProductC"
#
#     def create_object(self):
#         return self
#
#
# class Creator:
#     "The Factory Class"
#
#     @staticmethod
#     def create_object(some_property):
#         """ A static method to get a concrete product """
#         if some_property == "a":
#             return ConcreteProductA()
#         elif some_property == "b":
#             return ConcreteProductB()
#         elif some_property == "c":
#             return ConcreteProductC()
#         else:
#             return None
#
#
# product = Creator().create_object("c")
# print(product.name)
#
#

from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    """The Chair Interface (Product)"""

    @staticmethod
    @abstractmethod
    def get_dimensions():
        """A static interface method"""


class SmallChair(IChair):
    """The Small Chair Concrete Class implements the Ichair interface"""

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            "width": self._width,
            "height": self._height,
            "depth": self._depth,
        }
