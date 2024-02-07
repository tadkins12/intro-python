# Daily Warmup

# Create a new file called activityFeb7.py
# and answer the following questions

# 1. In your own words, what is a computer program?

A: "a computer program is a sequence or set of instructions in a programming language for a computer to execut"

# 2. Name three (3) data types
    
a: "boolean, float, data type"

# 3. Name three (3) python Operators

A: "assignment operators, Multiplication, identity operators"

# 4. In your own words, what is a variable?

A: "a container for data"

# READING PROMPTS
# Carefully read through each scenario and determine which Python Operator you would use to build the
# particular program. 

# Read the question carfully
# Find key words that you recognized to deduce what it could be
# use context clues provided in the prompt ot deduce what it could be.

# 5. You have been hired as a software engineer to develop a gym membership system.
# Your program needs to verify two (2) things; if the user is a member of the gym, AND
# if the user has the gold membership tier, which allows the user to have access to the swimming pool.
# What your client would like to happen is that when a user is a member AND 
# and also has the gold membership they should be able to use the pool.
# Which python operator would you use in this situation? Explain why

A:'logical operator - when 2 things are true, remain true
# keywords and context
# varifiy if they are a member AND a gold card member
# if both these things are TRUE give them access to thr pool. 

member = True
goldtier = false
silvertier = False
bronzetetier = False


print("can this person access the pool?")
print(member and goldtier)

# 6. You have been hired as a software engineer to develop a simple payment system for a companys 
# webstore. Your assignment is to create a cart system where the prices of all 
# the items are added together and then deducts a 20% discount at checkout. 
# Which python operator would you use in this situation? Explain why.

A:'arithmitic and assignment - arithmitc to calculate the prices
assingment to assign the prices to the cart'

apple= 10.00
socks= 20.00
books= 15.00


cart= apple + socks + books
cart a
print('total of cart:')
print(cart)

# 7. You have been hired as an engineer to develop a student badge system. Your client would like to 
# have a system where when a student swipes their badge, the ID number on the badge is compared to the ID
# number in the database.If the ID numbers match and are the same the student can come in, if it does not
# match, they cannot enter.
# Which python operator would you use in this situation? Explain why

A:' compairason operator because we want to see if they are the same/ compair

studentId = 12345'
database = 12345
 
print(database == studentId)
 
