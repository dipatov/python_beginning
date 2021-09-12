from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def expenses(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def expenses(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    @property
    def expenses(self):
        return self.height * 2 + 0.3


coat = Coat('Levis', 130)
print(coat.name, coat.size, coat.expenses)

suit = Suit('Gucci', 40)
print(suit.name, suit.height, suit.expenses)
