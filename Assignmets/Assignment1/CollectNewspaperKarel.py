"""
File: CollectNewspaperKarel.py
Name: Shane Liu
-------------------------
At present, the CollectNewspaperKarel file does nothing.

In the assignment, your job is to add the necessary code to:
(1) instruct Karel to walk to the door of its house, 
(2) pick up the newspaper(beeper), and then
(3) return to its initial position, the upper left corner of the house
"""

from karel.stanfordkarel import *


def main():
    """
    Karel moves to pick up the newspaper,
    and return to its initial position.
    """
    pick_newspaper()
    back_home()


def pick_newspaper():
    """
    pre-condition:  Karel is at (4,3), facing east
    post-condition: Karel is at (3,6), facing east and picking up the newspaper already
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def turn_right():
    """
    turn left 3 times
    """
    turn_left()
    turn_left()
    turn_left()


def back_home():
    """
    pre-condition:  Karel is at (3,6), facing east and picking up the newspaper already
    post-condition: Karel is at (4,3), facing east and putting down the newspaper
    """
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


if __name__ == '__main__':
    execute_karel_task(main)
