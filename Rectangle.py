from config import block_size


import pygame


class Rectangle:
    def __init__(self, size=(block_size, block_size), pos=(100, 100), clr=(255, 255, 255), border=0):
        self.size = size
        self.x = pos[0]
        self.y = pos[1]
        self.color = clr
        self.border_width = border

    def draw(self, display_surf):
        pygame.draw.rect(display_surf, self.color, (self.x, self.y, *self.size), self.border_width)