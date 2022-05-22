"""
File: reverse_string.py
Name: Shane Liu
-------------------------
The goal of this file is to reverse 'stressed'.
"""


def main():
	"""
	This program reverses 'stressed'.
	"""
	s = 'stressed'
	print(reverse(s))


def reverse(string):
	"""
	:param string: str, the word to be reversed
	:return result: str, reversed string
	"""
	result = ''
	for i in range(len(string)):
		result = string[i] + result
	return result


if __name__ == '__main__':
	main()
