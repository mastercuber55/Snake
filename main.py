import pygame
from pygame.locals import *

from Rectangle import Rectangle, rectangles_collide
from Snake import Snake
from config import window_size_x, window_size_y

def draw_grid(display_surf):
    for x in range(0, window_size_x, 32):
        pygame.draw.line(display_surf, (64, 64, 64), (x, 0), (x, window_size_y))
    for y in range(0, window_size_y, 32):
        pygame.draw.line(display_surf, (64, 64, 64), (0, y), (window_size_x, y))

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode((window_size_x, window_size_y))
        self.fps = pygame.time.Clock()
        self.frame = 0

        self.snake = Snake()
        self.foods = []
        
        for i in range(3):
            self.foods.append(Rectangle(clr=(255, 0, 0)))
        pygame.display.set_caption("Snake")

    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_draw()
        self.on_cleanup()


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):

        # self.frame += 1

        # if self.frame == 20:
        #     self.frame = 0

        moved = False 
        keys = pygame.key.get_pressed()

        self.snake.default_direction()

        if keys[K_w]:
            self.snake.direction["y"] = "top"
            moved = True
        if keys[K_a]:
            self.snake.direction["x"] = "left"
            moved = True
        if keys[K_s]:   
            self.snake.direction["y"] = "bottom"
            moved = True
        if keys[K_d]:
            self.snake.direction["x"] = "right"
            moved = True

        if moved:
            self.snake.handle_head()  

        for food in self.foods:
            if rectangles_collide(food, self.snake.head):
                self.snake.grow()
                self.foods.remove(food)

    def on_draw(self):
        self.display_surf.fill((0, 0, 0))  # Clear the screen with black color
        draw_grid(self.display_surf)

        self.snake.draw(self.display_surf)
        
        for food in self.foods:
            food.draw(self.display_surf)

        pygame.display.update()
        self.fps.tick(60)
    
    def on_cleanup(self):
        pygame.quit()

if __name__ == '__main__':
    myGame = Game()
    myGame.run()