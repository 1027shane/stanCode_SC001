"""
File: prime_checker.py
Name: Shane Liu
-------------------------
This program asks our user for input and checks if the input is a prime number or not,
as following steps:
(1) ” Welcome to the prime checker” will be printed on console
(2) the program will continually ask the user to enter an integer, greater than 1 
(3) checks if it is a prime number
(4) program ends when the user enter the EXIT number
"""

EXIT = -100


def main():

	print('Welcome to the prime checker!')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!')
			break
		# search for any common factor from 2 to n(entered number)
		temp = 2
		while n > temp:
			# when temp is n's factor,
			# n will be divided with no remainder
			if n % temp == 0:
				print(str(n)+' is not a prime number.')
				break
			temp += 1
		if n == temp:
			print(str(n) + ' is a prime number.')


if __name__ == "__main__":
	main()
