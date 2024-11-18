# Robert Feller
# 10/20/2024
# P3LAB
# Give user random cost and ask how much money they give, then give difference

# Convert the P3LAB code into a function
# Create the main function
# Generate a random cost, ask the user for cash, calculate and display change
# Run P3LAB code using change
# Run main function at end of code

#------------------------------------------------------------
# P3LAB converted to function for this program
def disperse_change(moneyCon):
    minusDollar = 0
    minusQuarter = 0
    minusDime = 0
    minusNickel = 0

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

    if (minusDime // 5) == 1:
        print((minusDime // 5), 'Nickel')
    elif (minusDime // 5) > 1:
        print((minusDime // 5), 'Nickels')
    minusNickel = minusDime - ((minusDime // 5) * 5)

    if (minusNickel // 1) == 1:
        print((minusNickel // 1), 'Penny')
    if (minusNickel // 1) > 1:
        print((minusNickel // 1), 'Pennies')
#------------------------------------------------------------

#------------------------------------------------------------
# Main function
def main():
    import random

    randomCost = round(random.uniform(0.01, 100.00), 2)
    userCash = ''
    cashCon = 0.0
    change = 0.0

    print(f'You owe ${randomCost}')

    userCash = input('How much cash will you put in the self-checkout? ')
    cashCon = float(userCash)

    change = cashCon - randomCost
    print(f'Change is: ${change:.2f}\n')

    disperse_change(change)
#------------------------------------------------------------

# Call main function
main()