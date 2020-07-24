single_quotes = 'You can use single quotes'
print(single_quotes)

double_quotes = "You can use double quotes"
print(double_quotes)

escaped_quotes = "You can\'t go wrong with \"escaped\" apostrophes and quotes"
print(escaped_quotes)

triple_quotes = """She said, "I guess you can use triple quotes!"
"AND IT'LL ESCAPE SINGLE OR DOUBLE QUOTES!!!", he yelled.
"Why are you yelling?", she asked.
"Because it preserves new lines and white space  ....   too", he whispered.
 """
print(triple_quotes)

# string concatenation
yum = "chocolate" + " and " + "marshmallows"
print(yum)  # output: chocolate and marshmallows

# string are immutable but you can append them
# which creates a new string
yum = yum + " and ice cream"
print(yum)  # output: chocolate and marshmallows and ice cream
# in place addition
yum += ", that sounds delicious"
print(yum)  # output: chocolate and marshmallows and ice cream, that sounds delicious

# you can use multiplication for string repetition
yum = yum + ("!" * 20)
print(yum)  # output: chocolate and marshmallows and ice cream, that sounds delicious!!!!!!!!!!!!!!!!!!!!

# string functions
# len() for length
quote = "A person who never made a mistake never tried anything new"
quote_length = len(quote)
print(quote_length)

# .upper() for uppercase
quote_uppercase = quote.upper()
print(quote_uppercase)

# .lower() for lowercase
quote_lowercase = quote.lower()
print(quote_lowercase)

# .title() for uppercase on all words first letter
quote_title = quote.title()
print(quote_title)

# str() to cast something to string type
calculations = 20 + 22
forty_two = str(calculations)
life_meaning = "The answer to the ultimate question of life, the universe, and everything is " + forty_two
print(life_meaning)

using_templates = "This is {} how you use templates {}"
using_templates = using_templates.format("probably", "my dude")
print(using_templates)
