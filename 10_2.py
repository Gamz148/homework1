from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_require(self):
        raise NotImplementedError

    @abstractmethod
    def add_to_reserve(self):
        raise NotImplementedError

    @abstractmethod
    def show_reserve(self):
        raise NotImplementedError


class Coat(Clothes):

    reserve_cloth = 0

    def __init__(self, size):
        self.size = size
        super().__init__("пальто")

    @property
    def cloth_require(self):
        return self.size*6.5 + 0.5

    @property
    def add_to_reserve(self):
        Coat.reserve_cloth += self.cloth_require


    def show_reserve(self):
        return self.reserve_cloth

class Suit(Clothes):
    reserve_cloth = 0

    def __init__(self, height):
        self.height = height
        super().__init__("костюм")

    @property
    def cloth_require(self):
        return self.height*2 + 0.3

    @property
    def add_to_reserve(self):
        Suit.reserve_cloth += self.cloth_require


    def show_reserve(self):
        return self.reserve_cloth


c1 = Coat(12)
c2 = Coat(1)
c3 = Coat(121)
c4 = Coat(23)
c1.add_to_reserve
c2.add_to_reserve
print(c1.cloth_require)
print(c2.cloth_require)
print(Coat.reserve_cloth)

s1 = Suit(12)
s2 = Suit(1)
s3 = Suit(121)
s4 = Suit(23)
s1.add_to_reserve
s2.add_to_reserve
print(s1.cloth_require)
print(s2.cloth_require)
print(Suit.reserve_cloth)
