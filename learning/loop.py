"""
Learning about loops
"""
from typing import Final

FAVORITES: Final = ["banku", "wakye", "eba"]

for idx, items in enumerate(FAVORITES):
    print(idx, items)

# FAVORITES = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisú", "Chocolate Cake"]


def while_loop() -> None:
    """while loop"""
    count = 0

    while count < len(FAVORITES):
        print("One of my favorite desserts is", FAVORITES[count])
        count += 1
