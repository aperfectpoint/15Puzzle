import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from puzzle15.game import Board
from puzzle15.tiling import init_tiles

"""
the user io is based on the curses library. it has a simple event loop, each iteration prints instructions (or game 
over) string and the board, then blocks and waits for a user's input. It sends the board the requested event and 
clears the terminal. 
input
"""

commands = "(n)ew game. (c)hars game. (s)mall game. (q)uit"
instructions = "welcome tp 15 Puzzle. Play by using the arrow keys. " + commands
finish = "congrats! you finished the game! " + commands


def main(stdscr):
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    # Enable easy key codes
    stdscr.keypad(True)

    from puzzle15 import tiling

    # creating an initial random board
    board = Board()

    while True:

        is_done = board.is_done()
        if is_done:  # printing the finish string
            stdscr.addstr(finish)
        else:  # printing the instructions string
            stdscr.addstr(instructions)
        # printing the board
        stdscr.addstr(str(board))

        c = stdscr.getch()
        """
        since the board semantics is based on a movement of the empty tile, but from the user perspective we're moving
        the surrounding tiles, the keyboard direction and board movements are opposites. 
        """
        if c == KEY_DOWN and not is_done:
            board.move_empty_tile_up()
        elif c == KEY_UP and not is_done:
            board.move_empty_tile_down()
        elif c == KEY_LEFT and not is_done:
            board.move_empty_tile_right()
        elif c == KEY_RIGHT and not is_done:
            board.move_empty_tile_left()
        elif c == 99:  # generate a new board with characters
            board = Board(init_tiles(tiling.id_2_char))
        elif c == 110:  # generate a new board with integers
            board = Board()
        elif c == 113:  # quit
            break
        elif c == 115:  # small 2x3 board
            board = Board(init_tiles(tiling.id_2_char, 6), 2, 3, 5)
        else:
            stdscr.addstr(str(c))
        stdscr.clear()


stdscr = curses.initscr()

curses.wrapper(main)
