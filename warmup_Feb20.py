#list of things that go in a grocery list

laundry= ['socks','pants','shirts','hats','waffles']

#print an item in index 3

def laundryindex():
    print(laundry[3])

laundryindex()

#create function that takes user name then prints
#steps to solves

# step 1: print out users name --> input()
# step 2: print out the user in reverse

def reversename():
    username = input('what is your name?')[::-1]
    print(username)

reversename()