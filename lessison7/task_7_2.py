from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def cons_cloth(self):
        pass


class Coat(Wear):
    def __init__(self, v):
        self._v = v

    @property
    def cons_cloth(self):
        return self._v / 6.5 + 0.5


class Suit(Wear):
    def __init__(self, h):
        self._h = h

    @property
    def cons_cloth(self):
        return self._h * 2 + 0.3


coat = Coat(5)
suit = Suit(10)
print(coat.cons_cloth+suit.cons_cloth)
