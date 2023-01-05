
class Entity:
    """
    A generic object to represent things in the demo
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, deltaX, deltaY):
        # Movement definition.  deltaX and deltaY indicate how much to move the x and y coordinates of the entity.
        self.x += deltaX
        self.y += deltaY
        # Checks for bounds?
        


