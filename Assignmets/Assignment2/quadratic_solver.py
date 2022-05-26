"""
File: quadratic_solver.py
Name: Shane Liu
-------------------------
This program should implement a console program that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
"""

import math


def main():
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	if a != 0:  # Restricts from variable "a" being zero

		discriminant = b*b-4*a*c
		
		if discriminant > 0:
			x1 = (-b+math.sqrt(discriminant))/(2*a)
			x2 = (-b-math.sqrt(discriminant))/(2*a)
			print('Two root: '+str(x1)+' , '+str(x2))
		elif discriminant < 0:
			print('No real roots')
		else:
			x = (-b+math.sqrt(discriminant))/(2*a)
			print('One root: '+str(x))
			
    else:
        print('The parameter \"a\" cannot be zero. Please start it over!')


if __name__ == "__main__":
	main()
