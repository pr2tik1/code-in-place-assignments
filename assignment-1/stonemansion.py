from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        turn_left()
        if no_beepers_present():
                put_beeper()
        move_up()
        turn_around()
        come_back()
        turn_left()
        if front_is_clear():
            move()
            move()
            move()
            move()
    last_time()

def last_time():
    turn_left()
    if no_beepers_present():
            put_beeper()
    move_up()
    turn_around()
    come_back()
    turn_left()
        
def come_back():
    while front_is_clear():
        if beepers_present():
            move()
        if no_beepers_present():
            put_beeper()
            move()

def move_up():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()   



if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')