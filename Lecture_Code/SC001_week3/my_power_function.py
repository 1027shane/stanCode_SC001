"""
File: my_power_function.py
Name: Shane Liu
-------------------------
This program shows how to make their own functions, 
by defining def my_power(a, b).
"""


def main():
	print('This program prints a to the power of b.')
	a = int(input('a: '))
	b = int(input('b: '))
	print(my_power(a, b))


def my_power(a, b):
	"""
	:param a: int, a>0
	:param b: int, b>=0
	:return: int, a**b(Python syntax)
	"""
	# Method 1:
	ans = 1
	for i in range(b):
		ans *= a
	return ans

	# Method 2:
	# if b == 0:
	# 	return 1
	# else:
	# 	ans = a
	# 	for i in range(b-1):
	# 		ans *= a
	# 	return ans


if __name__ == '__main__':
	main()
