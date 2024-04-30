# Quiz rules:

# This quiz is open book/ open note: you may use class notes, notes from the instructor github, w3schools.com as well as google to search for relevant articles
# You MAY NOT use chatgpt or any AI software for this quiz. Any usage of AI tools will result in an automatic failure.

# No phones are allowed during the quiz. Failure to put your phone away will result in an automatic failure.

# There is no talking during the quiz. 

# You will have the entire class period to complete the quiz. 

# To recieve full credit please show your work by providng clues, keywords, and notes you wrote down to solve
# the problem.  

# 1. What is a while loop, what is a for loop, and what is the difference between the two.
# Please write your response using complete sentences. 

# A while loop and a for loop are both programming constructs used for repetition or looping in code.
# While loops are generally used when you don't know in advance how many times you'll need to loop,
# while for loops are used when you know the number of iterations in advance or when you want to
# iterate over a sequence of values.

# 2. Name and describe three python operator families. Plese write your response using complete
# sentences.

# 3. Create a function that will accept 3 arguements. 
# This function should multiply the first 2 arguments 
# and then subtract the last argument from the sum of the first 2.

def multiply_and_subtract(a, b, c):
    # Multiply the first two arguments
    result = a * b
    # Subtract the third argument from the result
    result -= c
    return result

# Example usage:
print(multiply_and_subtract(5, 3, 2))  # Output: 13

 

# 4. Research the range() function. Then create a function that takes 2 arguements. 
# Your function should take the range of the first argument and multiply those numbers by the second 
# argument. 

#The range() function in Python generates a sequence of numbers within a specified range. It's commonly
# used in loops to iterate over a sequence of numbers. The syntax for range() is range(start, stop, step),
# where start is the starting number (default is 0), stop is the ending number (not inclusive), and step is 
# the difference between each number (default is 1).

def multiply_range(num_range, multiplier):
    """
    Multiply numbers in the given range by the multiplier.

    Arguments:
    num_range : range
        The range of numbers to be multiplied.
    multiplier : int
        The number to multiply each element in the range by.

    Returns:
    list
        List containing the result of multiplying each number in the range by the multiplier.
    """
    return [num * multiplier for num in num_range]

# Example usage:
result = multiply_range(range(1, 6), 2)
print(result)  # Output: [2, 4, 6, 8, 10]

# 5. Create a function that will ask the user guess the correct number.
# Your function should take a user input which will be their guess. Your function should 
# generate a random number between 1 and 5. If the user guesses the number correctly, the program
# will inform the user they guessed correctly and end the game. If the user guesses incorrectly, they
# will be informed their guess is incorrect and to guess again. The user should only be able to guess
# incorrectly 3 times. If they get the 3rd attempt wrong, the program should inform they user they have lost
# the game.

import random

def guess_number_game():
    # Generate a random number between 1 and 5
    target_number = random.randint(1, 5)
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        # Ask the user for their guess
        guess = int(input("Guess the number between 1 and 5: "))
        
        # Check if the guess is correct
        if guess == target_number:
            print("Congratulations! You guessed the correct number:", target_number)
            return  # End the game
            
        # If the guess is incorrect, inform the user and allow them to guess again
        print("Incorrect guess. Try again.")
        attempts += 1
        
    # If the user runs out of attempts
    print("Sorry, you've run out of attempts. The correct number was:", target_number)
    
# Call the function to start the game
guess_number_game()


# 6. Create a function that will act as a saving calculator. Your function should take several inputs from
# the user. Your program should ask the user what they are saving up for, how much does it cost, and how much 
# they want to deposit this week. Your program should repeat asking the user how much would they like to
# save this week, until the goal amount has been satisfied. Each time the user makes a deposit, your
# program should inform them how many weeks they have left, how much money they have deposited, and how
# much money their is remaining to reach their goal. 

def saving_calculator():
    # Ask user for goal and weekly deposit
    goal = float(input("What are you saving up for? "))
    cost = float(input("How much does it cost? "))
    deposit_this_week = float(input("How much would you like to deposit this week? "))

    # Initialize variables
    weeks_left = 0
    total_deposited = 0

    # Calculate weeks left
    while total_deposited < cost:
        total_deposited += deposit_this_week
        weeks_left += 1
        remaining_goal = cost - total_deposited
        print(f"Week {weeks_left}:")
        print(f"You have {weeks_left} week(s) left.")
        print(f"You have deposited ${total_deposited:.2f} so far.")
        print(f"You have ${remaining_goal:.2f} remaining to reach your goal.")

        # Ask for deposit this week
        deposit_this_week = float(input("How much would you like to save this week? "))

    print("Congratulations! You have reached your goal!")

saving_calculator()

# Ex. if my goal is to save $500, and deposit $20 dollars for that week, it should tell me that 
# It will take me 25 weeks to reach my goal based on the 20 dollar deposit, I have $20 saved,
# and that I need $480 more dollars.

# If I deposit $40 dollars the next week it should tell me
# it will take 10 weeks to reach my goal based on the $40 dollar deposit, I have $60 saved, and that I need 
# $440 more dollars to reach my goal.
