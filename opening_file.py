"""
Learning about files in python
"""


def without_with() -> None:
    "opening a file without the use of the with statement"
    file = open("file.txt", mode="r", buffering=1, encoding="utf-8")

    data = file.readline()

    print(data)
    file.close()


def with_with() -> None:
    "opening a file with the use of the with statement"
    with open("file.txt", mode="r", buffering=1, encoding="utf-8") as file:
        data = file.readline()
        print(data)


with_with()
