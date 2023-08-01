# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
import sys

if sys.version_info >= (3, 11, 0):
    from typing import Self
else:
    from typing_extensions import Self

from abc import ABC, abstractmethod


# Class Bank
class Bank(ABC):
    def basicinfo(self: Self) -> str:
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw(self: Self, amount: int) -> int:
        pass


# Class Swiss
class Swiss(Bank):
    def __init__(self: Self) -> None:
        self.__balance = 1000

    def basicinfo(self: Self) -> str:
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.__balance)

    def withdraw(self: Self, amount: int) -> int:
        if amount > self.__balance:
            print("Insufficient funds")
            return self.__balance

        self.__balance -= amount
        print(f"withdrawn amount: {amount}")
        print(f"New Balance: {self.__balance}")
        return self.__balance


# Driver Code
def main() -> None:
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)
    help(s)
    print(Swiss.mro())


if __name__ == "__main__":
    main()
