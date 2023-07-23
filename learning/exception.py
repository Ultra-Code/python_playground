"""
Learning exceptions
"""
import sys


def divide(numerator: float, denominator: float) -> float:
    """
    divide numerator by denominator and return result
    """
    try:
        return numerator / denominator
    except ZeroDivisionError as error:
        print(error, ": you can't divide by zero")
        sys.exit(1)
    except Exception as error:
        print("Error:", error)
        sys.exit(2)


print(divide(40, 0))
