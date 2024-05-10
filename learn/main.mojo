from mojofied import Struct, TraitStruct, fun_with_traits, repeat, sum, make_fast, count_many_things, print_many, print_nicely, min, add, describeDType, sets, dicts, optionals, MyPet
fn main():
    var int:Int = 0
    int = 3
    var new_struct = Struct("Fast")
    var new_trait = TraitStruct() 
    fun_with_traits(new_trait)
    print(new_struct.first_mojo())
    repeat[3]("Zig | Mojo | C23")
    print("Sum of 1,2,3 is ",sum(1,2,3))
    make_fast("Zig is ", "C23 is ", "Mojo might be ")
    print(count_many_things(5, 11.7, 12))
    print_many("Bob","Zig")
     # prints:
     # `a = 7`
     # `y = 8`
    print_nicely(a=7, y=8)
    min(1,2,3)
    add("st","ry")
    add(1,1.333)
    describeDType[DType.float32]()
    sets()
    dicts()
    optionals()
    var dog = MyPet("Charlie", 5)
    #Without the copy and move constructors, the following code would not
    #work because Mojo would not know how to copy an instance of MyPet
    var poodle = dog
    print(poodle.name)

