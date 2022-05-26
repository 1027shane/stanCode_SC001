"""
File: CheckerboardKarel.py
Name: Shane Liu
-------------------------
CheckerboardKarel should draw a checkerboard using beepers. 
Make sure that the program works for all of the sample worlds 
provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will draw a checkerboard using beepers.
    """
    put_beeper()
    while left_is_clear():
        fill_one_line()
        back_to_initial()
        cross()
    # OBOB situation
    fill_one_line()


def fill_one_line():
    """
    pre-condition:  Karel is at Avenue 1, facing east
    post-condition: Karel is at Avenue n, facing west
    """
    while front_is_clear():
        move()
        # check the last step to decide put or Not put beeper
        turn_around()
        move()
        if on_beeper():
            turn_around()
            move()
        else:
            turn_around()
            move()
            put_beeper()
    turn_around()


def cross():
    """
    pre-condition:  Karel is at Street n, facing north
    post-condition: Karel is at Street n+1, facing east
    """
    if on_beeper():
        move()
    else:
        move()
        put_beeper()
    turn_right()


def back_to_initial():
    """
    pre-condition:  Karel is at Avenue n, facing west
    post-condition: Karel is at Avenue 1, facing north
    """
    while front_is_clear():
        move()
    turn_right()


def turn_around():
    """
    turn left 2 times
    """
    turn_left()
    turn_left()


def turn_right():
    """
    turn left 3 times
    """
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    execute_karel_task(main)
