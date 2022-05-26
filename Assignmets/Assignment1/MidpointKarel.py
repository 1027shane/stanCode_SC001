"""
File: MidpointKarel.py
Name: Shane Liu
-------------------------
MidpointKarel should leave a beeper on the corner closest to the center of 1st Street,
or either of the two central corners if 1st Street has an even number of corners.
The world may be of any size, 
but you are allowed to assume that it is at least as tall as it is wide.

Tips:  
Karel can put down additional beepers as it looks for the midpoint, 
but must pick them up again before it stops.  
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will put a beeper closest to the center of 1st Street,
    through picking a pair(two) of beepers,
    the far left/right side of a line(combined with all beepers), once a time.
    """
    # for the world size in 1*1
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_around()
    pick_pair_beepers()


def pick_pair_beepers():
    """
    pre-condition:  Karel is at the (Street 1, Avenue n), facing west
    post-condition: Karel is on the corner closest to the center
    """
    if front_is_clear():
        # for the world size in 2*2
        pick_beeper()  # far right side beeper
        move()
        # for the world size in 3*3 or more
        if front_is_clear():
            while front_is_clear():
                move()
            turn_around()
            pick_beeper()  # far left side beeper
            move()

            while on_beeper():
                while on_beeper():
                    move()
                turn_around()
                move2steps()
                if on_beeper():
                    turn_around()
                    move()
                    turn_around()
                    pick_beeper()
                    move()
            # move to stand on the last beeper
            turn_around()
            move()


def move2steps():
    """
    move 2 times to make sure the beeper is last one,
    two sides are both empty(Not on beeper)
    """
    move()
    move()


def turn_around():
    """
    turn left 2 times
    """
    turn_left()
    turn_left()


if __name__ == '__main__':
    execute_karel_task(main)
