"""
File: nested_for_loop.py
Name: Shane Liu
-------------------------
This program shows the basic concepts of nested(double) for loop,
by printing a 4-row-3-col rectangle.
"""

# These constants control the diameter of the rectangle
ROW = 4  # The number of rows
COL = 3  # The number of cols


def main():
	for i in range(ROW):
		for j in range(COL):
			print('#', end="")
		print('')


if __name__ == '__main__':
	main()
