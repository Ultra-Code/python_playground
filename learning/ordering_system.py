"""
Excercise on datastructures and loops
"""
from typing import TypedDict, Final


class Order(TypedDict):
    """
    Orders
    """
    name: str
    price: float


MenuMap = dict[int, Order]
OrderList = list[Order]

menu: MenuMap = {
    1: {"name": "espresso", "price": 1.99},
    2: {"name": "coffee", "price": 2.50},
    3: {"name": "cake", "price": 2.79},
    4: {"name": "soup", "price": 4.50},
    5: {"name": "sandwich", "price": 4.99},
}


def calculate_subtotal(orders: OrderList) -> float:
    """Calculates the subtotal of an order

    [IMPLEMENT ME]
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print("Calculating bill subtotal...")
    ### WRITE SOLUTION HERE
    order_sum: float = 0
    for order in orders:
        order_sum += order["price"]
    return round(order_sum, 2)


def calculate_tax(subtotal: float) -> float:
    """Calculates the tax of an order

    [IMPLEMENT ME]
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded
        to two decimals.
    """
    print("Calculating tax from subtotal...")
    ### WRITE SOLUTION HERE
    return round(0.15 * subtotal, 2)


def summarize_order(orders: OrderList) -> tuple[list[str], float]:
    """Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable
        named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like

        return names, total

    """
    ### WRITE SOLUTION HERE
    order_names = []
    order_names = [item["name"] for item in orders]

    subtotal: Final = calculate_subtotal(orders)
    total = calculate_tax(subtotal) + subtotal

    return order_names, round(total, 2)


def print_order(order: OrderList) -> OrderList:
    """
    This function is provided for you, and will print out the items in an order
    """
    print("You have ordered " + str(len(order)) + " items")
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu() -> None:
    """
    This function is provided for you, and will display the menu
    """
    print("------- Menu -------")
    for order_no, food in menu.items():
        print(
            f"{order_no}. {food['name'] : <9}\
            | {food['price'] : >5}"
        )
    print()


def take_order() -> OrderList:
    """
    This function is provided for you, and will create an order
    by prompting the user to select menu items
    """
    display_menu()
    order = []
    count = 1
    for _ in range(3):
        item = input("Select menu item number " + str(count) + " (from 1 to 5): ")
        count += 1
        order.append(menu[int(item)])
    return order


def main() -> None:
    """
    main: fn
    """
    orders = take_order()
    print_order(orders)
    summarize_order(orders)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # items, subtotal = summarize_order(order)


if __name__ == "__main__":
    main()
