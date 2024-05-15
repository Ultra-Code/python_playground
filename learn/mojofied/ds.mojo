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


fn to_string(x: IntOrString) -> String:
    if x.isa[String]():
        return x[String]
    # x.isa[Int]()
    return str(x[Int])


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
    # If your type doesn't use any pointers for heap-allocated data
    # you can just add the @value decorator to your struct definition and Mojo
    # will synthesize the __init__(), __copyinit__(), and __moveinit__() methods
    var name: String
    var age: Int

    fn __del__(owned self):
        print("Destruct", self.name)


struct SynthesizedMyPet:
    var name: String
    var age: Int

    # The constructor must take ownership to store each value.
    # This is a useful micro-optimization and enables the use of move-only types
    fn __init__(inout self, owned name: String, age: Int):
        # The transfer operator is also just a formality in this case, because,
        # even if it's not used with self.name = name^, the Mojo compiler will
        # notice that name is last used here and convert this assignment into a
        # move, instead of a copy+delete.
        self.name = name^
        self.age = age

    # does not support implicit conversion
    # the constructor must be called with a keyword
    fn __init__(inout self, *, name: StringLiteral):
        self.name = name
        self.age = 0

    fn __copyinit__(inout self, existing: Self):
        self.name = existing.name
        self.age = existing.age

    fn __moveinit__(inout self, owned existing: Self):
        self.name = existing.name^
        self.age = existing.age


struct HeapArray:
    var data: Pointer[Int]
    var size: Int
    var cap: Int

    fn __init__(inout self, size: Int, val: Int):
        self.size = size
        self.cap = size * 2
        self.data = Pointer[Int].alloc(self.cap)
        for i in range(self.size):
            self.data.store(i, val)

    # Implement __copyinit__() with value semantics.HeapArray type that performs a deep copy in the copy constructor
    fn __copyinit__(inout self, existing: Self):
        # Deep-copy the existing value
        self.size = existing.size
        self.cap = existing.cap
        self.data = Pointer[Int].alloc(self.cap)

        for i in range(self.size):
            self.data.store(i, existing.data.load(i))
        # The lifetime of `existing` continues unchanged

    # When a move occurs, Mojo immediately invalidates the original `existing` variable, preventing any access to it and disabling its destructor. Invalidating the original variable is important to avoid memory errors on heap-allocated data, such as use-after-free and double-free errors.
    fn __moveinit__(inout self, owned existing: Self):
        print("move")
        # Shallow copy the existing value
        self.size = existing.size
        self.data = existing.data
        self.cap = existing.cap
        # Then the lifetime of `existing` ends here, but
        # Mojo does NOT call its destructor

    fn __del__(owned self):
        # We must free the heap-allocated data, but
        # Mojo knows how to destroy the other fields
        for i in range(self.size):
            # NOTE: not needed in this case since elements are Ints
            # ensure destructors are called on array elements. It does this by
            # assigning each of the stored values in turn to the _ "discard"
            # pattern. Assigning a value to the _ discard variable tells the
            # compiler that this is the last use of that value, so it can be
            # destroyed immediately
            _ = __get_address_as_owned_value((self.data + i).address)
        # You can force Mojo to keep a value alive up to a certain point by
        # assigning the value to the _ discard pattern at the point where it's
        # okay to destroy it
        self.data.free()

    fn append(inout heap_array: Self, val: Int):
        # Update the array for demo purposes
        if heap_array.size < heap_array.cap:
            heap_array.data.store(heap_array.size, val)
            heap_array.size += 1
        else:
            print("Out of bounds")

    fn dump(self):
        # Print the array contents for demo purposes
        print("[", end="")
        for i in range(self.size):
            if i > 0:
                print(", ", end="")
            print(self.data.load(i), end="")
        print("]")


struct GenericArray[T: AnyRegType]:
    var data: Pointer[T]
    var size: Int

    fn __init__(inout self, *elements: T):
        self.size = len(elements)
        self.data = Pointer[T].alloc(self.size)
        for i in range(self.size):
            self.data[i] = elements[i]

    fn __del__(owned self):
        self.data.free()

    fn __getitem__(self, i: Int) raises -> T:
        if i < self.size:
            return self.data[i]
        else:
            raise Error("Out of bounds")

    # Create a new array with count instances of the given value
    @staticmethod
    fn splat(count: Int, value: T) -> Self:
        ...


fn use_generic_array() raises:
    var array = GenericArray[Int](1, 2, 3, 4)
    for i in range(array.size):
        print(array[i], sep=" ", end="")


struct MyStruct:
    fn __init__(inout self):
        pass

    fn foo(inout self):
        print("calling instance menthod")

    @staticmethod
    fn foo():
        print("calling static method")


fn test_static_overload():
    var a = MyStruct()
    # `foo(inout self)` takes precedence over a static method.
    a.foo()
