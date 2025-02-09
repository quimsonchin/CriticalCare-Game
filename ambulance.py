import pygame
from settings import WIDTH, HEIGHT, AMBULANCE_SPEED, AMBULANCE_IMAGE

class Ambulance:
    def __init__(self):
        self.image = pygame.image.load(AMBULANCE_IMAGE) # load Ambulance image
        self.image = pygame.transform.scale(self.image, (50, 50)) # scale Ambulance image
        self.x = WIDTH // 2 - 25 # set x position
        self.y = HEIGHT - 100 # set y position
        self.speed = AMBULANCE_SPEED
        
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 50:
            self.x += self.speed
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        if direction == "down" and self.y < HEIGHT - 50:
            self.y += self.speed
            
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))