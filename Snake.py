from Rectangle import Rectangle
from config import block_size


class Snake:
    def __init__(self):
        self.head = Rectangle(clr=(255, 255, 255), pos=(300, 300))
        self.body = [self.head]

        self.default_direction()

        for i in range(5):
            self.body.append(Rectangle(pos=(self.head.x - i * block_size, self.head.y), clr=(0, 0, 255)))

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

        self.handle_tail()

    def handle_tail(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y