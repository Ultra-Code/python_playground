from mojofied import HeapArray


fn copies():
    var a = HeapArray(2, 1)
    var b = a  # Calls the copy constructor
    a.dump()  # Prints [1, 1]
    b.dump()  # Prints [1, 1]

    b.append(2)  # Changes the copied data
    b.dump()  # Prints [1, 1, 2]
    a.dump()  # Prints [1, 1] (the original did not change)


fn moves():
    var a = HeapArray(3, 1)

    a.dump()  # Prints [1, 1, 1]

    var b = a^  # Prints "move"; the lifetime of `a` ends here

    b.dump()  # Prints [1, 1, 1]
    # a.dump()  # ERROR: use of uninitialized value 'a'


fn pets():
    var a = MyPet("Loki", 4)
    var b = MyPet("Sylvie", 2)
    print(a.name)
    # a.__del__() runs here for "Loki"

    a = MyPet("Charlie", 8)
    # a.__del__() runs immediately because "Charlie" is never used

    print(b.name)
    # b.__del__() runs here
    var dog = MyPet("Charlie", 5)
    # Without the copy and move constructors, the following code would not
    # work because Mojo would not know how to copy an instance of MyPet
    var poodle = dog
    print(poodle.name)


fn use_two_strings():
    var pet = MyPet("Po", 8)
    print(pet.name)
    # pet.name.__del__() runs here, because this instance is
    # no longer used; it's replaced below

    pet.name = String("Lola")  # Overwrite pet.name
    print(pet.name)
    # pet.__del__() runs here


fn consume(owned arg: String):
    _ = arg
    ...


fn use(arg: MyPet):
    print(arg.name)


fn consume_and_use():
    var pet = MyPet("Selma", 5)
    consume(pet.name^)
    # pet.name.__moveinit__() runs here, which destroys pet.name
    # Now pet is only partially initialized

    # use(pet)  # This fails because pet.name is uninitialized

    pet.name = String("Jasper")  # All together now
    use(pet)  # This is ok
    # pet.__del__() runs here (and only if the object is whole)
