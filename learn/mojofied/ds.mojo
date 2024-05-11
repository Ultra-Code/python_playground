from utils import Variant
from collections import Set


fn lists():
    var list = List(2, 3, 5)
    list.append(7)
    list.append(11)
    print("Popping last item from list: ", list.pop())
    for idx in range(len(list)):
        print(list[idx], end=", ")


alias IntOrString = Variant[Int, String]


fn to_string(inout x: IntOrString) -> String:
    # if x.isa[String]():
    #     return x.get[String]()[]
    # x.isa[Int]()
    # return str(x.get[Int]()[])
    return ""


fn optionals():
    # Two ways to initialize an Optional with a value
    var opt1 = Optional(5)
    var opt2: Optional[Int] = 5
    # Two ways to initalize an Optional with no value
    var opt3 = Optional[Int]()
    var opt4: Optional[Int] = None
    var opt: Optional[String] = str("Testing")
    if opt:
        var value_ref = opt.value()
        print(value_ref[])
    var custom_greeting: Optional[String] = None
    print(custom_greeting.or_else("Hello"))

    custom_greeting = str("Hi")
    print(custom_greeting.or_else("Hello"))


fn sets():
    var i_like = Set("sushi", "ice cream", "tacos", "pho")
    var you_like = Set("burgers", "tacos", "salad", "ice cream")
    var we_like = i_like.intersection(you_like)
    print("We both like:")
    for item in we_like:
        print("-", item[])


fn dicts():
    var d = Dict[String, Float64]()
    d["plasticity"] = 3.1
    d["elasticity"] = 1.3
    d["electricity"] = 9.7
    for item in d.items():
        print(item[].key, item[].value)


fn use_to_string():
    # They have to be mutable for now, and implement CollectionElement
    var an_int = IntOrString(4)
    var a_string = IntOrString(String("I'm a string!"))
    var who_knows = IntOrString(0)
    import random

    if random.random_ui64(0, 1):
        who_knows.set[String]("I'm actually a string too!")

    print(to_string(an_int))
    print(to_string(a_string))
    print(to_string(who_knows))


@value
struct MyPet:
    # This is the same as SynthesizedMyPet
    var name: String
    var age: Int


struct SynthesizedMyPet:
    var name: String
    var age: Int

    fn __init__(inout self, owned name: String, age: Int):
        self.name = name^
        self.age = age

    fn __copyinit__(inout self, existing: Self):
        self.name = existing.name
        self.age = existing.age

    fn __moveinit__(inout self, owned existing: Self):
        self.name = existing.name^
        self.age = existing.age
