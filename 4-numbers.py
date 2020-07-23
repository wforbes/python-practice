integer = 1 + 3
print(integer)

floating_point = 1 + 3.5
print(floating_point)

what_is_this = 0.1 + 0.1 + 0.1 - 0.3
print(what_is_this)  # output: 5.551115123125783e-17

oh_its_zero = round(what_is_this)
print(oh_its_zero)

# round up
integer2 = round(4.6)
print(integer2)  # output: 5

# round down
integer3 = round(4.5)
print(integer3)  # output: 4

# PEMDAS order of operations
pemdas = 10 - 3 * 5 + 8
print(pemdas)
pemdas_parenthesis = (10 - 3) * (5 + 8)
print(pemdas_parenthesis)

# type error
# type_error = "apple" + 2
# print(type_error)
# TypeError: can only concatenate str (not "int") to str
# type_error2 = "2" + 2
# print(type_error2)
# type coersion
no_type_error = int("2") + 2
print(no_type_error)

# division resulting in float
floaty = 23 / 3
print(floaty)

# quotient with just the integer portion
inty = 23 // 3
print(inty)

# modulus to get the remainder
remainder = 23 % 3
print(remainder)
