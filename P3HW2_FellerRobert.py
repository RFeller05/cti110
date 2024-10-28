# Robert Feller
# 10/27/2024
# P3HW2
# Have the user input employee info and display calculated info

# Declare variables for the employee's info
# Ask the user for input and store it
# Calculate the extra information using the inputted information
# Display all information with proper formatting

# Post-Coding Note: Some format spacing is 14 instead of 15 to compensate the dollar sign

#--------------------------------
name = ""
hours = 0.0
payRate = 0.0

overTime = 0.0
overPay = 0.0
regPay = 0.0
grossPay = 0.0
#--------------------------------

#--------------------------------
name = input("Enter employee's name: ")
hours = input("Enter number of hours worked: ")
hours = float(hours)
payRate = input("Enter employee's pay rate: ")
payRate = float(payRate)
print("------------------------------------")
#--------------------------------

#--------------------------------
if hours > 40:
    overTime = hours - 40
    hours = 40
overPay = overTime * (payRate + (payRate * .5))
regPay = hours * payRate
grossPay = overPay + regPay
#--------------------------------

#--------------------------------
print(f'{"Employee Name:":15} {name}\n')
print(f'{"Hours Worked":<15} {"Pay Rate":<15} {"OverTime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
print("-----------------------------------------------------------------------------------------")
#                                             Should I put the comma here? v I know it's not needed but I think it looks better to separate the formats
print(f'{(hours + overTime):<15} {payRate:<15} {overTime:<15} ${overPay:<14,.2f} ${regPay:<14,.2f} ${grossPay:<14,.2f}')
#--------------------------------