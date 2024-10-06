# Robert Feller
# 10/6/2024
# P2LAB2
# Using a dictionary, accept user input for a vehicle, output its mpg, accept user input for miles, output needed gallons

# Create the dictionary
# Create user input variables and keys variable
# Print the keys, accept user input for car, and display MPG
# Accept user input for miles, calculate the gallons, and display

mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = mpg.keys()
carUI = ''
milesUI = ''
mpgCon = 0.0
gallons = 0.0

#-------------------------------------------------
print(keys, end='\n\n')

print('Enter a vehicle to see its mpg:', end=' ')
carUI = input()
mpgCon = f'{mpg[carUI]}'
mpgCon = float(mpgCon)
print('The', carUI, 'gets', mpgCon, 'mpg.', end='\n\n')

print(f'How many miles will you drive the {carUI}?', end=' ')
milesUI = input()
milesUI = float(milesUI)
gallons = milesUI / mpgCon
print(f'{gallons:.2f} gallon(s) of gas are needed to drive the {carUI} {milesUI} miles.')
#-------------------------------------------------