from python import Python
from math.limit import max_finite, min_finite
from utils import Variant
import testing

fn use_numpy() raises:
    var np = Python.import_module("builtin")

struct Struct:
    var name: String

    fn __init__(inout self, name:String):
        self.name = name

    fn first_mojo(self) -> String:
        return self.name + "Mojo"

    @staticmethod
    fn log_info(message: String):
        print("Info: ", message)

trait Traits:
    fn required(self, int:Int)->Int:...

@value
struct TraitStruct(Traits):
    fn required(self:TraitStruct, int:Int)->Int:
        return int

fn fun_with_traits[T: Traits](x: T):
    try:
        testing.assert_true(x.required(33) == 33)
    except:...

fn repeat[count:Int](msg:String):
    # @unroll directive only works if the loop limits are compile-time constants
    @unroll
    for _ in range(count):
        print(msg)

fn print_line():
    var long_text = "This is a long line of text that is a lot easier to read"
                    " if it is broken up across two lines instead of one long line."
    var text = String(",").join("Mojo", " Works")
    print(long_text)

fn pow(base: Int, exp: Int = 2) -> Int:
    return base ** exp

fn use_defaults():
    # Uses the default value for `exp`
    var z = pow(exp=10,base=2)
    print(z)

fn sum(*values: Int) -> Int:
    """
    Variadic function sum
    `*values`: is a variable list of int values.
    """
    var sum: Int = 0
    for value in values:
        sum = sum + value

    return sum

fn make_fast(owned * str:String):
    for item in str:
        print("{} Fast",item[])

fn count_many_things[*ArgTypes: Intable](*args: *ArgTypes) -> Int:
    var total = 0

    @parameter
    fn add[Type: Intable](value: Type):
        total += int(value)

    args.each[add]()
    return total

fn print_string(s: String):
    print(s, end="")

fn print_many[T: Stringable, *Ts: Stringable](first: T, *rest: *Ts):
    print_string(str(first))

    @parameter
    fn print_elt[T: Stringable](a: T):
        print_string(" ")
        print_string(a)

    rest.each[print_elt]()
    print("")

fn print_nicely(**kwargs: Int):
    try:
        for key in kwargs.keys():
          print(key[], "=", kwargs[key[]])
    except:...

fn min(a: Int, b: Int, /, *c:Int) -> Variant[Tuple[Int,VariadicList[Int]],Int]:
    return (a,c) if a < b else (b,c)

fn add(x: String, y: String) -> String:
    return x + y

fn add(x: Int, y: Int) -> Int:
    return x + y

fn vec():
    var vec1 = SIMD[DType.int8, 4](2, 3, 5, 7)
    var vec2 = SIMD[DType.int8, 4](1, 2, 3, 4)
    var product = vec1 * vec2
    print(product)

fn aliases():
    alias Scalar = SIMD[size=1]
    alias Int8 = Scalar[DType.int8]
    alias Float32 = Scalar[DType.float32]


fn describeDType[dtype: DType]():
    print(dtype, "is floating point:", dtype.is_floating_point())
    print(dtype, "is integral:", dtype.is_integral())
    print("Min/max finite values for", dtype)
    print(min_finite[dtype](), max_finite[dtype]())

fn bools():
    var conditionA = False
    var conditionB: Bool = not conditionA
    print(conditionA, conditionB)
