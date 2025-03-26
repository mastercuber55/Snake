from Rectangle import Rectangle
from config import block_size, window_size_x, window_size_y


class Snake:
    def __init__(self):
        self.head = Rectangle(clr=(255, 255, 255), pos=(block_size * 5, block_size * 3))
        self.body = [self.head]

        self.default_direction()

        for i in range(5):
            self.grow()
    
    def grow(self):
        last_part = self.body[-1]
        new_part = Rectangle(pos=(last_part.x, last_part.y), clr=(0, 0, 255))
        self.body.append(new_part)

    def default_direction(self):

        # Combination to achieve diagonal movement if needed
        self.direction = {
            # left, none, right
            "x": "none",
            # top, none, bottom
            "y": "none"
        }

    def draw(self, display_surf):
        for part in reversed(self.body):
            part.draw(display_surf)

    def handle_head(self):

        
        pos = (self.head.x, self.head.y)

        # Handle movement on the x axis
        if self.direction["x"] == "left":
            self.head.x -= block_size
        elif self.direction["x"] == "right":
            self.head.x += block_size

        #handle movement on the y axis
        if self.direction["y"] == "top":
            self.head.y -= block_size
        elif self.direction["y"] == "bottom":
            self.head.y += block_size

        if self.is_outside():
            self.head.x = pos[0]
            self.head.y = pos[1]
        else:
            self.handle_tail()

    def is_outside(self):
        
        x_condition = self.head.x < 0 or self.head.x > window_size_x - block_size
        y_condition = self.head.y < 0 or self.head.y > window_size_y - block_size

        return x_condition or y_condition

    def handle_tail(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y