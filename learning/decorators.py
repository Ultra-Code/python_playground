import typing


def my_decorator(func: typing.Callable[...]) -> typing.Callable:
    def wrapper() -> None:
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee() -> None:
    print("Whee!")


say_whee = my_decorator(say_whee)
