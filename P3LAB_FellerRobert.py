# Robert Feller
# 10/20/2024
# P3LAB
# Take user input for money and convert it to most efficient change

# Declare variables for each money type
# Take user input for the amount of money, convert it to double, multiply by 100, then convert to int
# If the inputted money is 0, display no change
# If the money is divisible by 100 for dollars, 25 for quarters, 10 for dimes, 5 for nickels, and 1 for pennies,->
# <-isolate the amount and subtract it from the total, then continue to the next

moneyUI = ''
moneyCon = 0.0
minusDollar = 0
minusQuarter = 0
minusDime = 0
minusNickel = 0

moneyUI = input('Enter the amount of money as a float: $')
moneyCon = float(moneyUI)
moneyCon = moneyCon * 100
moneyCon = int(moneyCon)

if moneyCon == 0:
    print('No change')

if (moneyCon // 100) == 1:
    print((moneyCon // 100), 'Dollar')
elif (moneyCon // 100) > 1:
    print((moneyCon // 100), 'Dollars')
minusDollar = moneyCon - ((moneyCon // 100) * 100)

if (minusDollar // 25) == 1:
    print((minusDollar // 25), 'Quarter')
elif (minusDollar // 25) > 1:
    print((minusDollar // 25), 'Quarters')
minusQuarter = minusDollar - ((minusDollar // 25) * 25)

if (minusQuarter // 10) == 1:
    print((minusQuarter // 10), 'Dime')
elif (minusQuarter // 10) > 1:
    print((minusQuarter // 10), 'Dimes')
minusDime = minusQuarter - ((minusQuarter // 10) * 10)

# Technically only this first one is needed as 2 nickels would be 1 dime
if (minusDime // 5) == 1:
    print((minusDime // 5), 'Nickel')
elif (minusDime // 5) > 1:
    print((minusDime // 5), 'Nickels')
minusNickel = minusDime - ((minusDime // 5) * 5)

if (minusNickel // 1) == 1:
    print((minusNickel // 1), 'Penny')
if (minusNickel // 1) > 1:
    print((minusNickel // 1), 'Pennies')