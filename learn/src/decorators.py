import logging
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar, Self

T = TypeVar("T")
P = ParamSpec("P")


# https://docs.python.org/3/library/typing.html?highlight=callable#typing.Callable
def my_decorator(func: Callable[P, T]) -> Callable[P, None]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> None:
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


def add_logging(func: Callable[P, T]) -> Callable[P, T]:
    """A type-safe decorator to add logging to a function."""

    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f"{func.__name__} was called")
        return func(*args, **kwargs)

    return inner


@add_logging
def add_two(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y


def say_whee() -> None:
    print("Whee!")


say_whee = my_decorator(say_whee)


class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self: Self, value: float) -> None:
        """Set radius, raise error if negative
        .radius is a mutable property: it can be set to a different value. However, by defining a
        setter method, we can do some error testing to make sure it`s not set to a nonsensical
        negative number. Properties are accessed as attributes without parentheses.
        """
        if value >= 0:
            self._radius = value
        else:
            msg = "Radius must be positive"
            raise ValueError(msg)

    @property
    def area(self):
        """Calculate area inside circle
        .area is an immutable property: properties without .setter() methods can`t be changed.
        Even though it is defined as a method, it can be retrieved as an attribute without
        parentheses
        """
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base
        .cylinder_volume() is a regular method
        """
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1
        .unit_circle() is a class method. It`s not bound to one particular instance of Circle.
        Class methods are often used as factory methods that can create specific instances of
        the class
        """
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though
        .pi() is a static method. It's not really dependent on the Circle class, except that it
        is part of its namespace. Static methods can be called on either an instance or the class
        """
        return 3.1415926535


c = Circle(5)
assert (c.radius) == 5

assert c.area == 78.5398163375

c.radius = 2
assert c.area == 12.566370614

# c.area = 100 #noqa: ERA001 #AttributeError: can't set attribute

assert c.cylinder_volume(height=4) == 50.265482456

# c.radius = -1 # ValueError: Radius must be positive #noqa: ERA001

c = Circle.unit_circle()
assert c.radius == 1

assert c.pi() == 3.1415926535

assert Circle.pi() == 3.1415926535

from dataclasses import dataclass


@dataclass
class PlayingCard:
    rank: str
    suit: str


def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat


@repeat(num_times=4)
def greet(name: str) -> None:
    print(f"Hello {name}")


add = lambda x, y: x + y  # noqa: E731
assert add(5, 3) == 8
assert (lambda x, y: x + y)(5, 3) == int(8)  # noqa: PLC3002

assert sorted(range(-5, 6), key=lambda x: x**2) == [
    0,
    -1,
    1,
    -2,
    2,
    -3,
    3,
    -4,
    4,
    -5,
    5,
]
