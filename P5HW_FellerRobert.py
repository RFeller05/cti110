# Robert Feller
# 11/24/2024
# P3LAB
# Gives the user simple math quizzes

# Displays the main menu and asks the user to choose an option
# When the user chooses 1 or 2, go to the functions, complete the math problem, then loop
# If the user enters 3, exit the loop and end the program
# If the user enters any other number, give an error and ask them to try again

#------------------------------------------------------------
# Functions for when the user chooses addition or subtraction
def addRandom():
    import random
    firstNumber = round(random.randint(0, 1000), 2)
    secondNumber = round(random.randint(0, 1000), 2)
    answer = firstNumber + secondNumber

    print(f"   {firstNumber}")
    print(f" + {secondNumber}")
    userAnswer = input("\nEnter answer: ")
    userAnswer = int(userAnswer)

    if userAnswer == answer:
        print("Wow! You got it first try!\n\n")

    guesses = 0

    while userAnswer != answer:
        if userAnswer > answer:
            print("Sorry, guess is too high.")
            userAnswer = input("\nTry again: ")
            userAnswer = int(userAnswer)
            guesses = guesses + 1
        elif userAnswer < answer:
            print("Sorry, guess is too low.")
            userAnswer = input("\nTry again: ")
            userAnswer = int(userAnswer)
            guesses = guesses + 1
    
    print("Congratulations!!! Your answer is correct.")
    print(f"Number of guesses: {guesses + 1}\n\n")

def subRandom():
    import random
    firstNumber = round(random.randint(0, 1000), 2)
    secondNumber = round(random.randint(0, 1000), 2)
    answer = firstNumber - secondNumber

    print(f"   {firstNumber}")
    print(f" - {secondNumber}")
    userAnswer = input("\nEnter answer: ")
    userAnswer = int(userAnswer)

    guesses = 0

    while userAnswer != answer:
        if userAnswer > answer:
            print("Sorry, guess is too high.")
            userAnswer = input("\nTry again: ")
            userAnswer = int(userAnswer)
            guesses = guesses + 1
        elif userAnswer < answer:
            print("Sorry, guess is too low.")
            userAnswer = input("\nTry again: ")
            userAnswer = int(userAnswer)
            guesses = guesses + 1
    
    print("Congratulations!!! Your answer is correct.")
    print(f"Number of guesses: {guesses + 1}\n\n")
#------------------------------------------------------------

#------------------------------------------------------------
# Main function
def main():
    print("Welcome to the Math Quiz\n")

    userChoice = 0

    while userChoice != 3:
        print("MAIN MENU")
        print("---------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")

        userChoice = input("Please choose one of the menu options: ")
        userChoice = int(userChoice)
        
        if userChoice == 1:
            addRandom()
        elif userChoice == 2:
            subRandom()
        elif userChoice == 3:
            print("Thank you for playing...")
            print("Bye!!!")
        else:
            print("Invalid choice, please try again\n\n")
#------------------------------------------------------------

main()