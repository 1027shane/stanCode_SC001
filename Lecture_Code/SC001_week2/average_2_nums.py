"""
File: average_2_nums.py
Name: Shane Liu
-------------------------
This file shows functions with/without parameters and return value.
There are two functions as bellow:
(1)intro() neither has params nor return value, while (2)my_average(a, b) has both.
"""


def main():
    """
    This program prints the average of 10 and 9 on Console.
    """
    intro()
    print('The average is: '+str(my_average(10, 9)))


def intro():
    """
    This function wraps 3 prints as intro().
    """
    print('Hello! Welcome!')
    print('This program averages 10 and 9')
    print('Have fun!')


def my_average(a, b):
    """
    :param a: int, the first number to be averaged
    :param b: int, the second number to be averaged
    :return ans: float, the average between a and b
    """
    ans = (a+b)/2
    return ans


if __name__ == '__main__':
    main()
