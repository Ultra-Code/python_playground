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


def create_file() -> None:
    "create a file with the `w` mode"
    try:
        with open("new_file.txt", mode="a", encoding="utf-8") as file:
            file.writelines(["\nThis is a great start\n", "Okay I am done"])
    except FileNotFoundError as error:
        raise error


create_file()
