from itertools import chain
from random import shuffle


class Tile:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class EmptyTile(Tile):
    def __init__(self):
        Tile.__init__(self, None)

    def __str__(self):
        return '*'


def init_tiles(number_of_tiles=16):
    """ initializes the tiles in order. """
    tiles = list()
    for i in range(number_of_tiles-1):
        tiles.append(Tile(i+1))
    # remove the last element
    tiles.append(EmptyTile())
    return tiles


class Board:

    def __init__(self, tiles_list=init_tiles(), rows=4, cols=4, empty_tile_id=4*4-1):
        self.rows = rows
        self.cols = cols
        self.tiles = dict()

        for i in range(len(tiles_list)):
            self.tiles[i] = tiles_list[i]

        self.empty_tile_id = empty_tile_id

        tiles_ids = list(self.tiles.keys())
        # randomize the game
        shuffle(tiles_ids)

        self.board = list()

        for row in range(rows):
            self.board.append(list())
            for col in range(cols):
                tile = tiles_ids[row * cols + col]
                self.board[row].append(tile)
                if tile == empty_tile_id:
                    self.empty_tile_position = row, col

    def is_done(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not (self.board[row][col] == row * self.cols + col):
                    return False
        return True

    def __str__(self):
        s = "\n"
        for row in range(self.rows):
            s += "\t".join(map(lambda tile_id: str(self.tiles[tile_id]), self.board[row]))
            s += "\n"
        return s

    def __move_empty_tile(self, predicate, movement):
        cur_x, cur_y = self.empty_tile_position
        if predicate(cur_x, cur_y):
            to = (cur_x + movement[0], cur_y + movement[1])
            self.__swap_tiles((cur_x, cur_y), to)
            self.empty_tile_position = to

    def move_empty_tile_up(self):
        self.__move_empty_tile(lambda x, y: x > 0, (-1, 0))

    def move_empty_tile_down(self):
        self.__move_empty_tile(lambda x, y: x < self.rows-1, (1, 0))

    def move_empty_tile_left(self):
        self.__move_empty_tile(lambda x, y: y > 0, (0, -1))

    def move_empty_tile_right(self):
        self.__move_empty_tile(lambda x, y: y < self.cols-1, (0, 1))

    def __swap_tiles(self, coords1, coords2):
        tmp = self.board[coords2[0]][coords2[1]]
        self.board[coords2[0]][coords2[1]] = self.board[coords1[0]][coords1[1]]
        self.board[coords1[0]][coords1[1]] = tmp


def flatmap(f, items):
    return chain.from_iterable(map(f, items))


if __name__ == '__main__':
    b = Board()
    print(str(EmptyTile()))