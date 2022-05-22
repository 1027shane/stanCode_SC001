"""
File: replace_keyword.py
Name: Shane Liu
-------------------------
This file shows how to replace old_word with new_word in old_s,
by calling replace function.
"""


def main():
	s = replace('Jerry hates coding', 'hates', 'teaches')
	print(s)


def replace(old_s, old_word, new_word):
	ans = ''
	if old_word not in old_s:
		print('Something went wrong!')
	else:
		i = old_s.find(old_word)
		ans += old_s[:i]
		ans += new_word
		ans += old_s[i+len(old_word):]
	return ans


if __name__ == '__main__':
	main()
