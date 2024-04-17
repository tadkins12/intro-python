# Warm up Tuesday April 16th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and Python While Loop.

#A for loop is typically used when you know the number of times you want to execute a 
#block of code or when you want to iterate over a sequence
#On the other hand, a while loop is used when you want to 
#repeat a block of code as long as a certain condition is true.


# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
# it should multiply that number by 3. 

numbers = [1, 2, 3, 4, 5]  # Example list of numbers

for number in numbers:
    result = number * 3
    print(result)


# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a random number for you. You must write a loop that will
# ask the user to input their guess, if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it correctly. Once they guess the correct number the program
# will congratulate them and the loop will stop.
 
 import random

def guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    while True:
        # Ask the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        
        # Check if the guess is correct
        if guess == target_number:
            print("Congratulations! You guessed the correct number:", target_number)
            break  # Exit the loop if the guess is correct
        elif guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

# Call the guessing_game function to start the game
guessing_game()


# generates a random number between 1 and 10
randomNumber = random.randint(1, 10)

print('Random number value is: {randomNumber}')