"""
File: find_max.py
Name: Shane Liu
-------------------------
This program finds the maximum among all the user inputs.
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among user inputs.
    """
    print('This program finds the max:')
    data = int(input('Data: '))
    if data == EXIT:
        print('No numbers')
    else:
        maximum = data
        while True:
            data = int(input('Data: '))
            if data == EXIT:
                break
            if data > maximum:
                maximum = data
        print('Max: ' + str(maximum))


if __name__ == '__main__':
    main()
