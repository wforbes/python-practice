# not equal
"potato" != "tomato" # returns True

# less than / greater than
6 > 3 # returns True
6 < 3 # returns False

# greater than or equal
42 >= 42 # returns True

# string comparison checks first letter value
"sunshine" > "rain" # returns True - S comes after R alphabetically


age = int(input("How old are you? "))
if age <= 6:
	print("You're {}? Whoa, you're good with computers!")
else:
	print("You smell like potatoes.")