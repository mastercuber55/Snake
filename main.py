import pygame
from pygame.locals import *

from Rectangle import Rectangle
from Snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode((640, 480))
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

    def on_draw(self):
        self.display_surf.fill((0, 0, 0))  # Clear the screen with black color
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