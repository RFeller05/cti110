# Robert Feller
# 10/6/2024
# P2LAB1
# Take user input and display circle details

# Get user input for the radius
# Do the math for diameter, circumference, and area
# Display each with the correct decimal places

import math

radius = ''
diameter = 0.0
circumference = 0.0
area = 0.0

#-------------------------------------------------
print('What is the radius of the circle?', end=' ')
radius = input()
radius = float(radius)

diameter = radius * 2
circumference = (2 * math.pi) * radius
area = math.pi * (radius ** 2)
#-------------------------------------------------

#-------------------------------------------------
print('The diameter of the circle is', f'{diameter:.1f}', end='\n')
print('The circumference of the circle is', f'{circumference:.2f}', end='\n')
print('The area of the circle is', f'{area:.3f}', end='\n')
#-------------------------------------------------