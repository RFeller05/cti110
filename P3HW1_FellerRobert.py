# Robert Feller
# 10/20/2024
# P3HW1
# Debugging the following program

# Get user input for each module grade
# Convert each to a float
# Create list and append each item into the list
# Get the list's minimum, maximum, sum, and average, then display
# Use an if statement to determine the user's letter grade and display

# Note: Left original comments intact

#-------------------------------------------------------

# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

mod_1 = float(mod_1)
mod_2 = float(mod_2)
mod_3 = float(mod_3)
mod_4 = float(mod_4)
mod_5 = float(mod_5)
mod_6 = float(mod_6)

# add grades entered to a list
grades = []
grades.append(mod_1)
grades.append(mod_2)
grades.append(mod_3)
grades.append(mod_4)
grades.append(mod_5)
grades.append(mod_6)

# TO DO: determine lowest, highest , sum and average for grades
print('\n--------------Results--------------')

low = min(grades)
print(f'{"Lowest Grade:":20} {low:.1f}')
high = max(grades)
print(f'{"Highest Grade:":20} {high:.1f}')
sum = sum(grades)
print(f'{"Sum of Grades:":20} {sum:.1f}')
avg = sum / len(grades)
print(f'{"Average:":20} {avg:.2f}')

# determine letter grade for average
print('-----------------------------------')
if avg >= 90:
   print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this