from config import block_size


import pygame


class Rectangle:
    def __init__(self, size=(block_size, block_size), pos=(100, 100), clr=(255, 255, 255), border=0):

        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
        
        self.color = clr
        self.border_width = border

    def draw(self, display_surf):
        pygame.draw.rect(display_surf, self.color, (self.x, self.y, self.w, self.h), self.border_width)


def rectangles_collide(a, b):

    x_condition = (a.x < (b.x + b.w) and (a.x + a.w) > b.x)
    y_condition = (a.y < (b.y + b.h) and (a.y + a.h) > b.y)

    collision = False

    if x_condition and y_condition:
        collision = True

    return collision