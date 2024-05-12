@register_passable("trivial")
struct MyInt:
    """A type that is implicitly convertible to `Int`."""

    var value: Int

    @always_inline("nodebug")
    fn __init__(inout int: Self, _a: Int):
        int.value = _a


fn foo[x: MyInt, a: Int]():
    print("foo[x: MyInt, a: Int]()")


fn foo[x: MyInt, y: MyInt]():
    print("foo[x: MyInt, y: MyInt]()")


fn bar[a: Int](b: Int):
    print("bar[a: Int](b: Int)")


fn bar[a: Int](*b: Int):
    print("bar[a: Int](*b: Int)")


fn bar[*a: Int](b: Int):
    print("bar[*a: Int](b: Int)")


fn parameter_overloads[a: Int, b: Int, x: MyInt]():
    # `foo[x: MyInt, a: Int]()` is called because it requires no implicit
    # conversions, whereas `foo[x: MyInt, y: MyInt]()` requires one.
    foo[x, a]()

    # `bar[a: Int](b: Int)` is called because it does not have variadic
    # arguments or parameters.
    bar[a](b)

    # `bar[*a: Int](b: Int)` is called because it has variadic parameters.
    bar[a, a, a](b)


fn use_parametric_overloaded():
    parameter_overloads[1, 2, MyInt(3)]()


fn concat[
    ty: DType, len1: Int, len2: Int
](lhs: SIMD[ty, len1], rhs: SIMD[ty, len2]) -> SIMD[ty, len1 + len2]:
    var result = SIMD[ty, len1 + len2]()
    for i in range(len1):
        result[i] = SIMD[ty, 1](lhs[i])
    for j in range(len2):
        result[len1 + j] = SIMD[ty, 1](rhs[j])
    return result


fn use_concat():
    var a = SIMD[DType.float32, 2](1, 2)
    var x = concat[DType.float32, 2, 2](a, a)

    print("result type:", x.element_type, "length:", len(x))


fn slice[
    ty: DType, new_size: Int, size: Int
](x: SIMD[ty, size], offset: Int) -> SIMD[ty, new_size]:
    var result = SIMD[ty, new_size]()
    for i in range(new_size):
        result[i] = SIMD[ty, 1](x[i + offset])
    return result


fn reduce_add[ty: DType, size: Int](x: SIMD[ty, size]) -> Int:
    # Use the @parameter decorator to create a parametric if condition,
    # which is an if statement that runs at compile-time. It requires that
    # its condition is a valid parameter expression, and ensures that only
    # the live branch of the if statement is compiled into the program
    @parameter
    if size == 1:
        return int(x[0])
    elif size == 2:
        return int(x[0]) + int(x[1])

    # Extract the top/bottom halves, add them, sum the elements.
    alias half_size = size // 2
    var lhs = slice[ty, half_size, size](x, 0)
    var rhs = slice[ty, half_size, size](x, half_size)
    return reduce_add[ty, half_size](lhs + rhs)


fn use_reduce_add():
    var x = SIMD[DType.index, 4](1, 2, 3, 4)
    print(x)
    print("Elements sum:", reduce_add(x))


fn parallelize[func: fn (Int) -> None](num_work_items: Int):
    # Not actually parallel: see the https://docs.modular.com/mojo/stdlib/algorithm/functional/parallelize module for api.
    for i in range(num_work_items):
        func(i)


struct MyType[s: String, i: Int, i2: Int, b: Bool = True]:
    pass


fn use_MyType():
    alias Bytes = SIMD[DType.uint8, _]
    _ = Bytes[8]()
    _ = MyType["Hello", 3, 4, True]
    alias a = MyType["Hola", _, _, True]
    _ = a[2, 3]
    # These two types are equivalent
    _ = MyType["Hello", *_]
    _ = MyType["Hello", _, _, _]
    # Unbound, with no parameters specified
    _ = MyType[_, _, _, _]


fn print_params(vec: SIMD[*_]):
    print(vec.type)
    print(vec.size)


fn same_as_print_params[t: DType, s: Int](vec: SIMD[t, s]):
    print(vec.type)
    print(vec.size)


fn auto_parameterization():
    var v = SIMD[DType.float64, 4](1.0, 2.0, 3.0, 4.0)
    print_params(v)


fn interleave(v1: SIMD, v2: __type_of(v1)) -> SIMD[v1.type, v1.size * 2]:
    var result = SIMD[v1.type, v1.size * 2]()
    for i in range(v1.size):
        result[i * 2] = SIMD[v1.type, 1](v1[i])
        result[i * 2 + 1] = SIMD[v1.type, 1](v2[i])
    return result


fn use_interleave():
    var a = SIMD[DType.int16, 4](1, 2, 3, 4)
    var b = SIMD[DType.int16, 4](0, 0, 0, 0)
    var c = interleave(a, b)
    print(c)


@value
struct Fudge[sugar: Int, cream: Int, chocolate: Int = 7](Stringable):
    fn __str__(self) -> String:
        var values = StaticIntTuple[3](sugar, cream, chocolate)
        return str("Fudge") + values


fn eat(f: Fudge[5, *_]):
    print("Ate " + str(f))


fn eat_expanded[cr: Int, ch: Int](f: Fudge[5, cream=cr, chocolate=ch]):
    print("Ate " + str(f))
