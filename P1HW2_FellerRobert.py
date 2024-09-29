# Robert Feller
# 9/29/2024
# P1HW2
# Take user input for travel details

# Create Variables for each user input, and one for the final balance
# Ask the user for all the required input while converting them
# Calculate the leftover balance by adding all of the user input together, and subtracting it from the budget UI
# Display everything

budget = ''
destination = ''
gasMoney = ''
accommodationCost = ''
foodCost = ''
leftoverBalance = 0

#-------------------------------------------------
print('This program calculates and displays travel expenses', end='\n\n')

print('Enter budget:', end=' ')
budget = input()
budget = float(budget)

print('Enter your travel destination:', end=' ')
destination = input()

print('Enter how much you think you will spend on gas:', end=' ')
gasMoney = input()
gasMoney = float(gasMoney)

print('Enter how much you will need for accomodations/hotel:', end=' ')
accommodationCost = input()
accommodationCost = float(accommodationCost)

print('Enter how much you will spend on food:', end=' ')
foodCost = input()
foodCost = float(foodCost)

leftoverBalance = budget - (gasMoney + accommodationCost + foodCost)
#-------------------------------------------------

#-------------------------------------------------
print('\n\n----------Travel Expenses----------', end='\n')

print('Location:', destination, end='\n')
print('Initial Budget:', budget, end='\n\n')

print('Fuel:', gasMoney, end='\n')
print('Accommodation:', accommodationCost, end='\n')
print('Food:', foodCost, end='\n\n')

print('Remaining Balance:', leftoverBalance)
#-------------------------------------------------