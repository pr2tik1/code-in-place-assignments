from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    put_beeper()
    take_steps()
    put_beeper()
    take_steps()
    put_beeper()
    take_steps()
    put_beeper()
    
def take_steps():
    move()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program('RampKarel1.w')