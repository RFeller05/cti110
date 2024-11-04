# Robert Feller
# 10/20/2024
# P3LAB
# Take user input for integer and display multiplication table for number

# Declare variables for storing the user's decision to run again or not and the user's number
# Only run the program is runAgain is equal to yes (it's yes by default)
# Ask the user for a number and if it is less than 0, display an error and ask if they want to run again
# If the number is positive, display the multiplication table for that number and ask if they want to run again
# If the user enteres anything other than yes, the program exits the loop and ends

runAgain = "yes"
userInput = 0;

while runAgain == "yes":
    userInput = input('Enter an integer: ')
    userInput = int(userInput)

    if userInput >= 0:
        for x in range(12):
            print(userInput, '*', (x + 1), '=', (userInput * (x + 1)))
        runAgain = input('Would you like to run the program again (yes/no)? ')
    
    else:
        print('This program does not handle negative numbers.')
        runAgain = input('Would you like to run the program again (yes/no)? ')
