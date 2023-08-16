from array import array
from collections import ChainMap, Counter, OrderedDict, defaultdict, namedtuple
from dataclasses import dataclass
from types import MappingProxyType
from typing import NamedTuple

writable = {"one": 1, "two": 2}
read_only = MappingProxyType(writable)

# The proxy is read-only:
print(read_only["one"])

# read_only["one"] = 23 # noqa: ERA001 #this would fail


dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = ChainMap(dict1, dict2)
print(chain["three"])


dd = defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")
print(dd["dogs"])


d = OrderedDict(one=1, two=2, three=3)

print(d)
OrderedDict([("one", 1), ("two", 2), ("three", 3)])

d["four"] = 4
print(d)
OrderedDict([("one", 1), ("two", 2), ("three", 3), ("four", 4)])

print(d.keys())


arr = array("f", (1.0, 1.5, 2.0, 2.5))
print(arr[1])

# Arrays are mutable:
arr[1] = 23.0
print(arr)

del arr[1]
print(arr)

arr.append(42.0)
print(arr)

# Strings can be unpacked into a list to
# get a mutable representation:
assert "".join(list("abcd")) == "abcd", "must be equal"

# bytes objects are immutable sequences of single bytes, or integers in the range 0 ≤ x ≤ 255.
byte = bytes((0, 1, 2, 3))
print(byte[1])


# Bytes literals have their own syntax:
assert byte == b"\x00\x01\x02\x03"

# The bytearray type is a mutable sequence of integers in the range 0 ≤ x ≤ 255.
barr = bytearray((0, 1, 2, 3))
assert barr[1] == 1

assert barr == b"\x00\x01\x02\x03"

# Bytearrays are mutable:
barr[1] = 23
assert barr == b"\x00\x17\x02\x03"

# Bytearrays can grow and shrink in size:
del barr[1]
assert barr == b"\x00\x02\x03"

barr.append(42)
assert barr == b"\x00\x02\x03*"

# Bytearrays can be converted back into bytes objects:
# (This will copy the data)
assert (copy_barr_bytes := bytes(barr)) == b"\x00\x02\x03*"


@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool


car1 = Car("red", 3812.4, automatic=True)


Point = namedtuple("Point", "x y z")  # python 2
point_1 = Point(1, 2, 3)
point_2 = (1, 2, 3)
assert point_1 == point_2


class CarImproved(NamedTuple):  # python 3
    color: str
    mileage: float
    automatic: bool


car_improved = CarImproved("red", 3812.4, automatic=True)

vowels = {"a", "e", "i", "o", "u"}
assert ("e" in vowels) is True

letters = set("alice")
assert letters.intersection(vowels) == {"a", "e", "i"}

vowels.add("x")
assert vowels == {"i", "a", "u", "o", "x", "e"}

fvowels = frozenset({"a", "e", "i", "o", "u"})
# fvowels.add("p") #noqa: ERA001

# Frozensets are hashable and can
# be used as dictionary keys:
fset = {frozenset({1, 2, 3}): "hello"}
assert fset[frozenset({1, 2, 3})] == "hello"

# The collections.Counter class in the Python standard library implements a multiset, or bag,
# type that allows elements in the set to have more than one occurrence


inventory: Counter = Counter()

loot = {"sword": 1, "bread": 3}
inventory.update(loot)
assert sorted(inventory.elements()) == ["bread", "bread", "bread", "sword"]
more_loot = {"sword": 1, "apple": 1}
inventory.update(more_loot)
assert inventory == Counter({"bread": 3, "sword": 2, "apple": 1})
assert inventory.total() == int(6)
