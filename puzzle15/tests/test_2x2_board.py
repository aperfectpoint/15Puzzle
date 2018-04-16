import random
import unittest

import puzzle15.tiling
from puzzle15 import game, tiling


class Test2x2Board(unittest.TestCase):
    """ tests a given small board by fixing a seed"""

    def setUp(self):

        random.seed(0)
        tiles = puzzle15.tiling.init_tiles(tiling.id_2_num, 4)
        self.board = game.Board(tiles, 2, 2, 3)
        self.original_x, self.original_y = self.board.empty_tile_position
        print(str(self.board))

    def test_move_up(self):
        self.board.move_empty_tile_up()
        self.assertEqual(self.board.empty_tile_position, (self.original_x-1, self.original_y))

    def test_move_down_illegal(self):
        self.board.move_empty_tile_down()
        self.assertEqual(self.board.empty_tile_position, (self.original_x, self.original_y))

    def test_move_left(self):
        self.board.move_empty_tile_left()
        self.assertEqual(self.board.empty_tile_position, (self.original_x, self.original_y-1))

    def test_move_right_illegal(self):
        self.board.move_empty_tile_right()
        self.assertEqual(self.board.empty_tile_position, (self.original_x, self.original_y))

    def test_move_up_and_down(self):
        self.board.move_empty_tile_up()
        self.board.move_empty_tile_down()
        self.assertEqual(self.board.empty_tile_position, (self.original_x, self.original_y))

    def test_move_left_and_right(self):
        self.board.move_empty_tile_left()
        self.board.move_empty_tile_right()
        self.assertEqual(self.board.empty_tile_position, (self.original_x, self.original_y))

    def test_winning_move(self):
        self.board.move_empty_tile_left()
        self.assertFalse(self.board.is_done())
        self.board.move_empty_tile_up()
        self.assertFalse(self.board.is_done())
        self.board.move_empty_tile_right()
        self.assertFalse(self.board.is_done())
        self.board.move_empty_tile_down()
        self.assertTrue(self.board.is_done())


if __name__ == '__main__':
    unittest.main()
