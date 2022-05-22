"""
File: my_upper.py
Name: Shane Liu
-------------------------
This file shows how python built-in s.upper() is implemented.
"""


def main():
	s = '123JeRrY123'
	print(upper(s))


def upper(s):
	ans = ''
	# loop over a string
	for i in range(len(s)):
		if s[i].islower():
			ans += s[i].upper()
		else:
			ans += s[i]
	return ans


if __name__ == '__main__':
	main()
