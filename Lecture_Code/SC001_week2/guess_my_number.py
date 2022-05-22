"""
File: guess_my_number.py
Name: Shane Liu
-------------------------
This program plays a Console game "Guess My Number",
which asks user to input a number until he/she gets it.
"""

# This constant controls when to stop the game
SECRET = 30


def main():
    print('Guess the number from 0-99')
    # Method 1:
    while True:
        guess = int(input('Your guess: '))
        if guess > SECRET:
            print('Too high!')
        elif guess < SECRET:
            print('Too low!')
        else:
            break

    # Method 2:
    # guess = int(input('Your guess: '))
    # while guess != SECRET:
    #     if guess > SECRET:
    #         print('Too high!')
    #     else:
    #         print('Too low!')
    #     guess = int(input('Your guess: '))

    print('Congrats! The secret: ' + str(SECRET))


if __name__ == '__main__':
    main()
