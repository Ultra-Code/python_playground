lists: list[int | str | bool] = [1, 2, "a", True]

nested: list[int | list[int]] = [1, [1]]

print(*lists)
print(nested, sep=",")

lists.insert(len(lists), "Inserted")
print(*lists)

lists.append("Appended")

print(*lists)

lists.extend([2, True, "Extended"])
print(*lists)

lists.pop(len(lists) - 1)
print(*lists)

del lists[len(lists) - 1]


tuples: tuple[int, int, str, bool] = (1, 1, "1", True)
tuples_no_bracket: tuple[int, str, bool] = 1, "1", True

assert tuples.count("1") == 1, f"check count is supposed to be {tuples.count('1')}"

print(tuples.index(1))

sets: set[int] = {1, 2}
sets.discard(2)
sets.add(6)
sets.remove(6)

sets_2: set[int] = {2}
new_set = sets.union(sets_2)
print(sets)
print(new_set)
print(new_set | {3, 4})  # union

print(sets.intersection(sets_2) == (sets & sets_2))
print(sets.difference(sets_2) == (sets - sets_2))
print(sets.symmetric_difference(sets_2) == (sets ^ sets_2))


# no duplicates are allowed and same key insertion overwrites previous
dicts: dict[str, int] = {"one": 1, "two": 2}
print(dicts["one"])
dicts["two"] = 3
del dicts["one"]

for key in dicts:
    print(key)

for key, values in dicts.items():
    print(key, values)

for values in dicts.values():
    print(values)


def sums(a: int, b: int) -> int:
    return a + b


def sum_all(args: tuple[int, ...]) -> int:
    sum: int = 0
    for value in args:
        sum += value
    return sum


def sum_all_a(*args: int) -> int:
    sum: int = 0
    for value in args:
        sum += value
    return sum


print(sum_all((1, 2, 3, 4, 5, 6, 7)))
print(sum_all_a(1, 2, 3, 4, 5, 6, 7))


def sum_all_d(kwargs: dict[str, int]) -> int:
    sum: int = 0
    for _, value in kwargs.items():
        sum += value
    return sum


def sum_all_da(**kwargs: int) -> int:
    sum: int = 0
    for _, value in kwargs.items():
        sum += value
    return sum


print(sum_all_d({"one": 1, "two": 2}))
print(sum_all_da(one=1, two=2))
