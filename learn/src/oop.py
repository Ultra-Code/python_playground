from typing import Self


class Alpha:
    c = 3.0

    def __new__(cls: type[Self]) -> Self:
        pass

    # constructor
    def __init__(self: Self) -> None:
        self._a = 2.0  # Protected member `a`
        self.__b = 2.0  # Private member `b`


a = Alpha()


class Fruit:
    def __init__(self, fruit: str) -> None:
        print("Fruit type: ", fruit)


class FruitFlavour(Fruit):
    def __init__(self: Self) -> None:
        super().__init__("Apple")
        print("Apple is sweet")


apple = FruitFlavour()
