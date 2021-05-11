from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""

def place_beepers_in_row():
    while front_is_clear():
        move()
        put_beeper()
def turn_around():
    turn_left()
    turn_left()
def remove_last():
    pick_beeper()
    move()
def move_to_next_end():
    while beepers_present():
        move()
    turn_around()
    move()    
def find_midpoint():
    turn_around()
    while beepers_present():
        remove_last()
        move_to_next_end()

def main():
    place_beepers_in_row()
    find_midpoint()
    put_beeper()

if __name__ == '__main__':
    run_karel_program()