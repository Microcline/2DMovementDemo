from map_objects.tile import Tile
from map_objects.rectangle import Rect
from random import randint

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # "Why are we changing the False to True? Before, we were setting every Tile to be walk-able by default, 
        # so that we could move around easily. Hence, we passed False to the Tile class, so that the blocked attribute would be False."
        # From http://rogueliketutorials.com/tutorials/tcod/2019/part-3/
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        # Creates rooms for demo purposes
        rooms = []
        num_rooms = 0
        for r in range(max_rooms):
            # random width and height, can change later
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random position without going out of the boundaries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)
            # Rectangle for generalization and ease of use
            new_room = Rect(x, y, w, h)
            # Loop through other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # No intersections
                self.create_room(new_room)
                # Get center coords
                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                    # This is the first room where the player starts
                    player.x = new_x
                    player.y = new_y
                else:
                    # All rooms after the first: connect to previous room with a tunnel

                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    if randint(0, 1) == 1:
                        self.create_horizontal_tunnel(prev_x, new_x, prev_y)
                        self.create_vertical_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_vertical_tunnel(prev_y, new_y, new_x)
                        self.create_horizontal_tunnel(prev_x, new_x, prev_y)
                rooms.append(new_room)
                num_rooms += 1
                        


    def create_room(self, room):
        # Go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_horizontal_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_vertical_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
            

    


    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
            
        return False