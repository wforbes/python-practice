first_name = input("What is your first name? ")
print("Hello,", first_name)

# 'if' keyword, with equality operator '=='
if first_name == "Will":
    print(first_name, "is learning Python")
elif first_name == "Jim":
    print(first_name, "is learning with fellow students at TeamTreehouse.com!")
else: # 'else' keyword
    print("You should totally learn Python, {}!".format(first_name))
print("have a great day {}!".format(first_name))