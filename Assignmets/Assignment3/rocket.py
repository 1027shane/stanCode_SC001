"""
File: rocket.py
Name: Shane Liu
-------------------------
This program should implement a console program that draws ASCII art, a rocket.
Moreover, the size of rocket is determined by a constant SIZE.
"""

# This constant determines rocket size.
SIZE = 10


def main():
	"""
	This rocket consist of 6 parts: 2 heads, 2 belts, 1 upper body and 1 lower body.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):
		temp = ''
		for j in range(SIZE-i):
			temp += ' '
		for j in range(i+1):
			temp += '/'
		for j in range(i+1):
			temp += '\\'
		print(temp)


def belt():
	temp = ''
	for i in range(SIZE*2):
		temp += '='
	print('+'+temp+'+')


def upper():
	for i in range(SIZE):
		temp = ''
		for j in range(SIZE-i-1):
			temp += '.'
		for j in range(i+1):
			temp += '/\\'
		for j in range(SIZE-i-1):
			temp += '.'
		print('|'+temp+'|')


def lower():
	for i in range(SIZE):
		temp = ''
		for j in range(i):
			temp += '.'
		for j in range(SIZE-i):
			temp += '\\/'
		for j in range(i):
			temp += '.'
		print('|'+temp+'|')


if __name__ == "__main__":
	main()
