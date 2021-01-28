# import keyword brings in a seperate library/module
import math

# returning a value from a function uses the return keyword
def split_check(total, number_of_people):
	cost_per_person = total / number_of_people
	return cost_per_person

amount_due = split_check(42.69, 4)
print("Each person owes ${}".format(amount_due))

print("with rounding and user input...")
def split_check_rounded(total, number_of_people):
	return math.ceil(total / number_of_people)

total_due = float(input("What is the total? "))
number_of_people = int(input("How many people? "))
amount_due = split_check_rounded(total_due, number_of_people)
print("Each person owes ${}".format(amount_due))

# code challenge.. demonstrate creating and calling a function

# Create a function named square that defines a single parameter named number 
# 	and returns the square of the value that was passed in
def square(number):
	return number * number

result = square(3)