

"""
The __init__ function takes the x and y coordinates of the top left corner,
and computes the bottom right corner based on the w and h parameters (width
and height). We’ll be adding more to this class shortly, but to get us 
started, that’s all we need.
"""
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
