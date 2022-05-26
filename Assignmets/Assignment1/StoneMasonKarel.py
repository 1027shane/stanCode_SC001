"""
File: StoneMasonKarel.py
Name: Shane Liu
-------------------------
At present, the StoneMasonKarel file does nothing.

In the assignment, your job is to add the necessary code to:
(1) instruct Karel to build a column, 
    a vertical structure that is 5 beepers tall in each avenue(arch).
(2) end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    In any world, Karel will build a column in each avenue
    and stop at (Street 1, Avenue n), facing east.
    """
    while front_is_clear():
        # Karel will on the bottom left side of arch, facing east
        turn_left()
        go()
        cross()
        # Karel will on the upper right side of arch, facing east
        turn_right()
        go()
        turn_left()
        turn_left()
        # Karel will on the bottom right side of arch, facing east
        if front_is_clear():
            cross()


def go():
    """
    before moving forward, decided to put or Not to put beepers.
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    # OBOB situation
    if not on_beeper():
        put_beeper()
    turn_right()


def turn_right():
    """
    turn left 3 times
    """
    turn_left()
    turn_left()
    turn_left()


def cross():
    """
    move from the left side to right side of arch
    """
    move()
    move()
    move()
    move()


if __name__ == '__main__':
    execute_karel_task(main)
