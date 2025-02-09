import pygame
import random
from settings import WIDTH, OBSTACLE_SPEED, OBSTACLE_IMAGE

class Obstacle:
    def __init__(self,y):
        self.image = pygame.image.load(OBSTACLE_IMAGE) # load Obstacle image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = random.randint(0, WIDTH - 50) # set x position
        self.y = y
        self.speed = OBSTACLE_SPEED
        self.direction = random.choice(["left", "right"])
        
    def move(self):
        if self.direction == "left":
            self.x -= self.speed
            if self.x < 0:
                self.x = WIDTH - 50
        else:
            self.x += self.speed
            if self.x > WIDTH - 50:
                self.x = 0
                
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))