from random import shuffle

from puzzle15.tiling import init_tiles


class Board:
    """
    the Board holds the actual state of the game. It is represented by a 2d matrix (in the given sizes), where each cell
    holds only the id of the tile. This allows a complete separation of the logic and the contents of a tile.
    This relation is accomplished by having a map between the tile ids and the actual tiles.
    Notice that this could have been done outside this class, but for simplicity it is here.

    In order to get a random board, we shuffle the tiles ids (until we get a none-winning permutation).
    After the shuffle, each tile id is inserted to its random location in the board, which is:
    index-in-shuffle = row * num_of_cols + column

    For example, on the default board (4x4), the 5th tile will be place in row 1, col 0 (notice we're indexing
    0-based, so the 5th tile is in the 4th index of the shuffled list).

    All the game mechanics are based on the empty tile, since all of its surrounding tiles are the only tiles that can
    be moved. The id of the empty tile is by default the last 1 (15), but it doesn't have to be.

    MOVEMENT:
    As mentioned, the movements mechanics are based on the empty tile's surroundings. So from the board perspective,
    we always move the empty tile rather then its surrounding tiles. This simplifies the edge-case semantics.

    """
    def __init__(self, tiles_list=init_tiles(), rows=4, cols=4, empty_tile_id=4 * 4 - 1):

        self.rows = rows
        self.cols = cols
        self.tiles = dict()

        for i in range(len(tiles_list)):
            self.tiles[i] = tiles_list[i]

        self.empty_tile_id = empty_tile_id

        tiles_ids = list(self.tiles.keys())

        tiles_ids = shuffle_excluding_given_order(tiles_ids)

        self.board = list()

        for row in range(rows):
            self.board.append(list())
            for col in range(cols):
                tile = tiles_ids[row * cols + col]
                self.board[row].append(tile)
                if tile == empty_tile_id:
                    self.empty_tile_position = row, col

    def is_done(self):
        """
        a tile is considered in place if its id corresponds to its location (row X num_cols + col).
        we're done when all ids are inplace
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if not (self.board[row][col] == row * self.cols + col):
                    return False
        return True

    def __str__(self):
        """
        the simplest representation of the board - iterate in order and spit out the value of the tile id
        """
        s = "\n"
        for row in range(self.rows):
            s += "\t".join(map(lambda tile_id: str(self.tiles[tile_id]), self.board[row]))
            s += "\n"
        return s

    def __move_empty_tile(self, predicate, movement):
        """
        a helper function for moving the empty tile. It receives a predicate on the coordinates of the empty tile.
        The predicate checks if the move is legal (e.g., not moving out of bounds).

        If the predicate is true, the empty tile swaps location with the tile in (empty-tile coords) + movement

        """
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
        """
        helper function to swap tie ids byu their coordinates
        """
        tmp = self.board[coords2[0]][coords2[1]]
        self.board[coords2[0]][coords2[1]] = self.board[coords1[0]][coords1[1]]
        self.board[coords1[0]][coords1[1]] = tmp


def shuffle_excluding_given_order(nums):
    """
    since there's a chance of getting the original list in a random shuffle, we need to take care of this option.
    the idea is to give the randomness 100 tries to shuffle. If it still fails to generate a legal shuffle
    (which can happen but with very low probability), the run is considered erroneous and we throw an exception.
    """
    shuffled = False

    shuffles_count = 0
    ordered_nums = list(nums)

    while not shuffled:
        # randomize the game
        shuffle(nums)
        for index in range(len(nums)):
            if nums[index] != ordered_nums[index]:
                shuffled = True
                break
        shuffles_count += 1
        print(shuffles_count)
        if shuffles_count > 100:
            raise Exception('something is bad with your randomness')

    return nums


if __name__ == '__main__':
    ll = list([1, 1])
    print(shuffle_excluding_given_order(ll))
