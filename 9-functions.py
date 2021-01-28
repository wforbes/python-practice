# without using functions... repetitive code
praise = "You are awesome"
praise = praise.upper()
number_of_characters = len(praise)
result = praise + "!" * (number_of_characters // 2)
print(result)

advice = "Don't forget to ask for help"
advice = advice.upper()
number_of_characters = len(advice)
result = advice + "!" * (number_of_characters // 2)
print(result)

advice2 = "Don't Repeat Yourself. Keep things DRY"
advice2 = advice2.upper()
number_of_characters = len(advice2)
result = advice2 + "!" * (number_of_characters // 2)
print(result)

# functions use the def keyword - short for define
#	and a colon to start the function body
def yell(text):
	print()
	print("yell function:")
	text = text.upper()
	number_of_characters = len(text)
	result = text + "!" * (number_of_characters // 2)
	print(result)

yell("You are awesome")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself. Keep things DRY")