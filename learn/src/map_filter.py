# ruff: noqa: ERA001
menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

# bad
# map(lambda coffee: (coffee[0] == "c" and coffee), menu)
# good
c_menu = [(coffee[0] == "c" and coffee or None) for coffee in menu]

print(c_menu)

# bad
# filter(lambda coffee: coffee[0] == "c" and coffee, menu)
# good
c_menu_filter = [coffee for coffee in menu if coffee[0] == "c"]
print(c_menu_filter)

# bad
# import functools
# pairs = [(1, "a"), (2, "b"), (3, "c")]
# functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
# good
pairs = [(1, "a"), (2, "b"), (3, "c")]
assert sum(x for x, _ in pairs) == 6

# Dictionary Comprehension
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using two input lists
months_dict = {key: value for (key, value) in zip(number, months, strict=True) if value[0] == "A"}
print("Using two lists: ", months_dict)

# Set Comprehension
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)
