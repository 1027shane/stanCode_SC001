"""
File: hangman.py
Name: Shane Liu
-------------------------
This program plays hangman game.
Users sees a dashed word, trying to correctly figure the un-dashed word out,
by inputting one character each round.
If the input is correct, show thecupdated word on console. 
Players have N_TURNS chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will randomly come up with a vocabulary,
    and the user can pick either one of the 26 alphabets for a guess.
    If the alphabet you pick is in the vocabulary, this program will show you the relative position(s). 
    If not, you lose one guess.
    
    The game ends either you guess all the alphabets right(win),
    or used up all N_TURNS guesses.
    """
    # answer = random_word()
    answer = 'BUNDLE'
    life = N_TURNS

    # dashed word
    dashed = ''
    for i in range(len(answer)):
        dashed += '_'

    while True:
        print('The world looks like: ' + dashed)
        print('You have '+str(life)+' guesses left.')
        # case-insensitive
        input_ch = input('Yore guess: ').upper()
        # illegal format:
        # (1) put longer than 1 letter in your guess
        # (2) put number in your guess
        if len(input_ch) != 1 or not input_ch.isalpha():
            print('illegal format')
        else:
            guess_right = False
            new_dashed = ''
            for i in range(len(answer)):
                if answer[i] == input_ch:
                    new_dashed += answer[i]
                    guess_right = True
                else:
                    new_dashed += dashed[i]
            dashed = new_dashed

        # Update life
        if guess_right:
            print('You are correct!')
        else:
            life -= 1
            print('There is no '+input_ch+'\'s in the word.')

        # Check if the game is over
        if life == 0:
            print('You are completely hung : (')
            break
        if '_' not in dashed:
            print('You win!!')
            break

    print('The word was: ' + answer)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
