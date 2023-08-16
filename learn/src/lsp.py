list_of_learning_materials = [
    "https://inventwithpython.com/blog/2022/11/19/python-linter-comparison-2022-pylint-vs-pyflakes-vs-flake8-vs-autopep8-vs-bandit-vs-prospector-vs-pylama-vs-pyroma-vs-black-vs-mypy-vs-radon-vs-mccabe/"
    "https://dev.to/tusharsadhwani/the-comprehensive-guide-to-mypy-561m",
    "https://docs.python.org/3/library/typing.html",
]

# multi variable declaration
a, b, c = 1, 2, 3

name: str = "hello"

from typing import TypeAlias, List

Vector: TypeAlias = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])


def double(n: int) -> int:
    return n * 2


num = double(21)
print(num)
# hello
# del a, b
fl = 3.2


ed = {a: "a", b: 4.2}
ass: bool = True
type({3, "hello", 4.2})

z: complex = 10 + 10j
z = 1.2


# casting fuction
def casting() -> None:
    ord("c")
    hex(0x1)
    oct(1)
    float()
    int()
    set()
    list()
    dict()
    tuple()


champ = "champ"
money = "money"
print(f"hello {champ} i want {money}", sep="|")
