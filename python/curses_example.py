#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses

"""
pad = curses.newpad(100, 100)
#  These loops fill the pad with letters; this is
# explained in the next section
for y in range(0, 100):
    for x in range(0, 100):
        try:
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
        except curses.error:
            pass

#  Displays a section of the pad in the middle of the screen
pad.refresh(0,0, 5,5, 20,75)
"""


screen = curses.initscr()

"""
Usually curses applications turn off automatic echoing of keys to the
screen, in order to be able to read keys and only display them under
certain circumstances. This requires calling the noecho() function.
"""
curses.noecho()

"""
If your application doesn’t need a blinking cursor at all, you can call
curs_set(0) to make it invisible.
"""
curses.curs_set(0)

"""
Terminals usually return special keys, such as the cursor keys or navigation
keys such as Page Up and Home, as a multibyte escape sequence.  Enable keypad
mode to return such sequences as special values such as curses.KEY_LEFT.
"""
screen.keypad(1)

while True:
    event = screen.getch()
    if event == ord("n"):
        screen.clear()
        screen.addstr("This is a NN\n\n")
    else:
        screen.clear()
        screen.addstr("This is a Sample Curses Script\n\n")
    if event == ord("q"):
        break

"""
Then call the endwin() function to restore the terminal to its original
operating mode.
"""
curses.endwin()
