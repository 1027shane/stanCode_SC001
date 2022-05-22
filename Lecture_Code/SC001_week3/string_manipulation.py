"""
File: string_manipulation.py
Name: Shane Liu
-------------------------
The goal of this file is to change 'stancode' to 'stanCode',
and show you how to do string manipulations by the following 3 steps:
(1) Start with an empty str
(2) Loop over the old str
(3) Concatenation
"""


def main():
	# Method 1:
	s = 'stancode'
	ans = ''
	for i in range(len(s)):
		alphabet = s[i]
		if alphabet == 'c':
			ans += 'C'
		else:
			ans += alphabet
	print(ans)

	# Method 2:
	# s = 'scancode'
	# ans = ''
	# for i in range(len(s)):
	# 	alphabet = s[i]
	# 	if i == 4:
	# 		ans += 'C'
	# 	else:
	# 		ans += alphabet
	# print(ans)


if __name__ == '__main__':
	main()
