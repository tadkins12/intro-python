# Complete the following questions. This assignment must be submitted
# on Monday April 15th, 2024, by 11:59pm to recieve full credit. 

#1. Look up and read about the Range keyword on W3 schools. 
# Do the "try now" example provided on the article page and in your async document, 
# in your own words, describe what the range() function does.  

# Prompt # 1 
# Create a python list of fruits. 
# Your list of fruits should contain mainly apples, organges,
# and a few other random fruits of your choice. 
# Once you have your list, create a python function that 
# uses a python For loop to go through the fruit list. 
# If the loop runs into a fruit with the value of apple, send 
# that value to a new list variable called apple list. If the loop encounter 
# a fruit with the value of orange, it should move the item to 
# a new list variable called orange list. Else, if the loop encounters
# any other fruit, it should move that item to a list called unsorted fruits.

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

def sort_fruits(fruit_list):
    apple_list = []
    orange_list = []
    unsorted_fruits = []

    for fruit in fruit_list:
        if fruit == "apple":
            apple_list.append(fruit)
        elif fruit == "orange":
            orange_list.append(fruit)
        else:
            unsorted_fruits.append(fruit)

    return apple_list, orange_list, unsorted_fruits

# List of fruits
fruits = ["apple", "orange", "apple", "banana", "orange", "grape", "apple", "kiwi"]

# Sorting the fruits
apple_list, orange_list, unsorted_fruits = sort_fruits(fruits)

print("Apple List:", apple_list)
print("Orange List:", orange_list)
print("Unsorted Fruits:", unsorted_fruits)
# Note: In order to recieve the minimum amount of credit, 
# write down any clues or keywords that you recognize in the prompt 
# and describe how you would solve this problem if you get stuck. 