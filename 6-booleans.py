# any non-zero number is true, zero is false
bool(1) # true
bool(42) # true
bool(0) # false

# python uses truthy/falsy concepts
# strings are true
bool("potato") # true
# empty strings are false
bool("") # false

# true and false keywords use uppercase first char
True
False

# negating a boolean with 'not' keyword
not True # false
not False # true

# the 'and' operator
True and True and True # true
True and True and False # false

# the 'or' operator
False or True # true
False or False # false

# parenthesis to order operations
(False or False or True) and (True and False) # false
(False or False or True) and not (True and False) # true
