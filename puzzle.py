#!/usr/bin/env python
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

import game
from game import Board


instructions = "welcome tp 15 Puzzle. Play by using the arrow keys. (n)ew game. (q)uit"
finish = "congrats! you finished the game! (n)ew game. (q)uit"


def main(stdscr):
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    # Enable easy key codes
    stdscr.keypad(True)

    board = Board(game.init_tiles(6), 2, 3, 5)

    while True:

        is_done = board.is_done()
        if is_done:
            stdscr.addstr(finish)
        else:
            stdscr.addstr(instructions)
        stdscr.addstr(str(board))

        c = stdscr.getch()

        if c == KEY_DOWN and not is_done:
            board.move_empty_tile_up()
        elif c == KEY_UP and not is_done:
            board.move_empty_tile_down()
        elif c == KEY_LEFT and not is_done:
            board.move_empty_tile_right()
        elif c == KEY_RIGHT and not is_done:
            board.move_empty_tile_left()
        elif c == 110:
            print('new game')
            board = Board(game.init_tiles(6), 2, 3, 5)
        elif c == 113:
            print("exit")
            break
        else:
            print(c)
        stdscr.clear()


stdscr = curses.initscr()

curses.wrapper(main)
