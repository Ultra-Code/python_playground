from typing import Final

favorites: Final = ["banku", "wakye", "eba"]

for idx, items in enumerate(favorites):
    print(idx, items)

favorite = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisú", "Chocolate Cake"]

count = 0

while count < len(favorite):
    print("One of my favorite desserts is", favorite[count])
    count += 1


