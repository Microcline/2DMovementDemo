from map_objects.tile import Tile
from map_objects.rectangle import Rect

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # "Why are we changing the False to True? Before, we were setting every Tile to be walk-able by default, so that we could move around easily. Hence, we passed False to the Tile class, so that the blocked attribute would be False."
        # From http://rogueliketutorials.com/tutorials/tcod/2019/part-3/
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self):
        # Creates rooms for demo purposes
        room1 = Rect(20, 15, 10, 15) # Arbitrary dimensions
        room2 = Rect(35, 15, 10, 15)

        self.create_room(room1)
        self.create_room(room2)

    def create_room(self, room):
        # Go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
            
        return False