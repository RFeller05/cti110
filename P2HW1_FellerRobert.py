# Robert Feller
# 10/13/2024
# P2HW1
# Take user input for travel details, but better display

# Create Variables for each user input, and one for the final balance
# Ask the user for all the required input while converting them
# Calculate the leftover balance by adding all of the user input together, and subtracting it from the budget UI
# Display everything using f-string width formatting

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
print('\n\n-------------Travel Expenses-------------', end='\n')
print(f'{"Location:":20} {destination}', end='\n')
print(f'{"Initial Budget:":20} ${budget:,.2f}', end='\n')
print(f'{"Fuel:":20} ${gasMoney:,.2f}', end='\n')
print(f'{"Accommodation:":20} ${accommodationCost:,.2f}', end='\n')
print(f'{"Food:":20} ${foodCost:,.2f}', end='\n')
print('-----------------------------------------', end='\n\n')

print(f'{"Remaining Balance:":20} ${leftoverBalance:,.2f}')
#-------------------------------------------------