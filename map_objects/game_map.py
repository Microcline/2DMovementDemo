from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # "Why are we changing the False to True? Before, we were setting every Tile to be walk-able by default, so that we could move around easily. Hence, we passed False to the Tile class, so that the blocked attribute would be False."
        # From http://rogueliketutorials.com/tutorials/tcod/2019/part-3/
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
            
        return False