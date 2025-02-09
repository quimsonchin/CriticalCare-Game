import pygame
from settings import WIDTH, HEIGHT, SCROLL_SPEED
from ambulance import Ambulance
from obstacle import Obstacle
from game_functions import handle_events, check_collision, draw_objects

#Initialize pygame
pygame.init()

#Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Critial Care")

ambulance = Ambulance()
obstacles = [Obstacle(y) for y in range(0, HEIGHT, 100)]

score = 0
background_y = 0
clock = pygame.time.Clock()

running = True
while running:
    running = handle_events(ambulance)
    
    for obstacle in obstacles:
        obstacle.move()
        
    if check_collision(ambulance, obstacles):
       print("Game Over! Score: ", score)
       running = False
       
    if ambulance.y < HEIGHT // 2:
        score += 1
        background_y += SCROLL_SPEED
        for obstacle in obstacles:
            obstacle.y += SCROLL_SPEED
            if obstacle.y > HEIGHT:
                obstacle.y = 0
        
    draw_objects(screen, ambulance, obstacles, score, background_y)
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()