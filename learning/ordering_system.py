from typing import Final, TypedDict


class Order(TypedDict):
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
    print("Calculating bill subtotal...")
    order_sum: float = 0
    for order in orders:
        order_sum += order["price"]
    return round(order_sum, 2)


def calculate_tax(subtotal: float) -> float:
    print("Calculating tax from subtotal...")
    return round(0.15 * subtotal, 2)


def summarize_order(orders: OrderList) -> tuple[list[str], float]:
    order_names = []
    order_names = [item["name"] for item in orders]

    subtotal: Final = calculate_subtotal(orders)
    total = calculate_tax(subtotal) + subtotal

    return order_names, round(total, 2)


def print_order(order: OrderList) -> OrderList:
    print("You have ordered " + str(len(order)) + " items")
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu() -> None:
    print("------- Menu -------")
    for order_no, food in menu.items():
        print(
            f"{order_no}. {food['name'] : <9}\
            | {food['price'] : >5}",
        )
    print()


def take_order() -> OrderList:
    display_menu()
    order = []
    count = 1
    for _ in range(3):
        item = input("Select menu item number " + str(count) + " (from 1 to 5): ")
        count += 1
        order.append(menu[int(item)])
    return order


def main() -> None:
    orders = take_order()
    print_order(orders)
    summarize_order(orders)


if __name__ == "__main__":
    main()
