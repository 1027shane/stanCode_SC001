"""
File: hailstone.py
Name: Shane Liu
-------------------------
This program should implement a console program
that simulates the execution of the Hailstone sequence,defined by Douglas Hofstadter.

Output format should match what is shown in the sample run as bellow:
17 is odd, so I make 3n+1: 52
52 is even, so I make half: 26
...
...
...
2 is even, so I make half: 1
It took 12 steps to reach 1.
"""


def main():
    """
    This program simulates the execution of the Hailstone sequence,
    asking for user input an int(n) and repeating following command till 1:
    --> If n is odd : n*3+1
    --> If n is even: n*2
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    # counter: to count the steps through n to 1
    counter = 0
    while n != 1:
        if n % 2 == 0:
            print(str(n)+' is even, so I take half: '+str(n//2))
            n = n//2
        else:
            print(str(n) + ' is odd, so I make 3n+1: ' + str(n*3+1))
            n = n*3+1
        counter += 1
    print('It took '+str(counter)+' steps to reach 1.')


if __name__ == "__main__":
    main()
