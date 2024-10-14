# Robert Feller
# 10/13/2024
# P2HW2
# Ask the user for grades and display calculated info

# List to store all inputted grades along with a variables for user input, min value, max value, sum, and average
# Ask the user for each grade, convert it to float, then store it in the list
# Get the lowest value, highest value, sum of list, and calculate average using sum and length
# Display all with correct spacing


grades = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
gradeUI = ''
minGrade = 0.0
maxGrade = 0.0
listSum = 0.0
average = 0.0

#----------------------------------------------------
print('Enter grade for Module 1:', end=' ')
gradeUI = input()
gradeUI = float(gradeUI)
grades[0] = gradeUI

print('Enter grade for Module 2:', end=' ')
gradeUI = input()
gradeUI = float(gradeUI)
grades[1] = gradeUI

print('Enter grade for Module 3:', end=' ')
gradeUI = input()
gradeUI = float(gradeUI)
grades[2] = gradeUI

print('Enter grade for Module 4:', end=' ')
gradeUI = input()
gradeUI = float(gradeUI)
grades[3] = gradeUI

print('Enter grade for Module 5:', end=' ')
gradeUI = input()
gradeUI = float(gradeUI)
grades[4] = gradeUI

print('Enter grade for Module 6:', end=' ')
gradeUI = input()
gradeUI = float(gradeUI)
grades[5] = gradeUI
#----------------------------------------------------

#----------------------------------------------------
minGrade = min(grades)
maxGrade = max(grades)
listSum = sum(grades)
average = listSum / len(grades)
#----------------------------------------------------

#----------------------------------------------------
print('\n--------------Results--------------')
print(f'{"Lowest Grade:":20} {minGrade:.1f}')
print(f'{"Highest Grade:":20} {maxGrade:.1f}')
print(f'{"Sum of Grades:":20} {listSum:.1f}')
print(f'{"Average:":20} {average:.2f}')
print('-----------------------------------')
#----------------------------------------------------