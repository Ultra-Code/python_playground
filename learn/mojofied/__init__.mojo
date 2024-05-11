# A mojo package called mojofied to be used in other modules

# NOTE: This simplifies imports from `from mojofied.init import Struct` to
# `from mojofied import Struct`
from .init import (
    Struct,
    TraitStruct,
    fun_with_traits,
    repeat,
    sum,
    make_fast,
    count_many_things,
    print_many,
    print_nicely,
    min,
    add,
    describeDType,
)

# NOTE: alternative to the above `from .ds import sets,dicts,optionals,MyPet`
from .ds import *
