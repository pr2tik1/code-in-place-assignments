from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_around()
    go_back()

def turn_around():
    turn_left()
    turn_left()

def go_back():
    while front_is_clear():
        move()
    turn_around()
    turn_left()
    while front_is_clear():
        move()
    turn_around()

if __name__ == '__main__':
    run_karel_program('Puzzle.w')
