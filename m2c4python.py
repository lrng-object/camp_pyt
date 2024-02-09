#1)
#In order to use the decimal datype
from decimal import Decimal
#Import math.[ceil(),sqrt()]
import math


some_list = ["Some", "fun", "list"]
some_tuple = ("Some", "fun", "tuple")
some_dictionary = {
    1 : "one",
    2 : "two",
    3 : "three"
}
some_integer = 512
some_float = 3.1415
some_decimal =  Decimal(142541.155415)

#2)
print("float = ",some_float)
print("rounded up = ",math.ceil(some_float))

#3)
print("square root =", math.sqrt(some_float))

#4)
print(list(some_dictionary.items())[0])

#5)
print(some_tuple[1])

#6)
some_list.append("Today")
print(some_list)
#7)
some_list[0] = "not"
print(some_list)

#8)sort() alphabetically by default, key param is used to ignore capital letters , could be: key = str.lower
some_list.sort()
print(some_list)

some_list.sort(key = str.capitalize)
print(some_list)

#9)
print("Original tuple", some_tuple)
some_tuple += ("there",)
print("Reasigned tuple" ,some_tuple)

