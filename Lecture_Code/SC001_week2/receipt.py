"""
File: receipt.py
Name: Shane Liu
-------------------------
This program calculates the meal cost and prints the result on Console.
"""


def main():
    meal = int(input('How much was the meal? '))
    tax = float(input('Tax: '))
    total = meal*(1+tax)
    print('Total: '+str(total)+'!')


if __name__ == '__main__':
    main()
