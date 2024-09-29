# Robert Feller
# 9/29/2024
# P1HW1
# Takes user input for calculating an exponent and addition/subtraction

baseValue = ''
exponent = ''
final1 = 0

startInt = ''
addInt = ''
subInt = ''
final2 = 0

#------------------------------------------------------
print('-----Calculating Exponents-----', end='\n')

print('Enter an integer as the base value:', end=' ')
baseValue = input()
print('Enter an integer as the exponent:', end=' ')
exponent = input()

baseValue = int(baseValue)
exponent = int(exponent)
final1 = baseValue ** exponent

print(baseValue, 'raised to the power of', exponent, 'is', final1, end='\n\n')
#------------------------------------------------------

#------------------------------------------------------
print('-----Addition and Subtraction-----', end='\n')

print('Enter a starting integer:', end=' ')
startInt = input()
print('Enter an interger to add:', end=' ')
addInt = input()
print('Enter an integer to subtract:', end=' ')
subInt = input()

startInt = int(startInt)
addInt = int(addInt)
subInt = int(subInt)
final2 = startInt + addInt - subInt

print(startInt, '+', addInt, '-', subInt, 'is equal to', final2)
#------------------------------------------------------