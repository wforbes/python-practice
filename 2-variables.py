# variables don't require any type keyword in their declaration
first_name = "Will"
print(first_name)

# variables can change type after they're set
first_name = 42
print(first_name)

# strings can be declared with single or double quotes
last_name = 'Forbes'
print(last_name)

# variable names must start with a letter or underscore
# they can't start with a number
# 4bes = "error" # gives SyntaxError: invalid decimal literal

# variable names can only contain alpha-numeric and underscores
# they can't contain any other symbols or spaces
# %bes = "error"  # gives SyntaxError: invalid syntax

# variable names are case sensitive
FIRST = "Will"
fIrSt = "William"
print(FIRST, fIrSt)  # output: Will William

# You can assign the same variable to multiple values in one line
first = middle = last = "Marcia"
print(first, middle, last)

# You can assign multiple values ot multiple variables in one line
first, middle, last = "William", "Alexander", "Forbes"
print(first)
print(middle)
print(last)
