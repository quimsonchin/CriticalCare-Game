from turtle import Screen
import pygame
from settings import HEIGHT, WHITE, BLACK, RED, GREEN, FONT_STYLE, WIDTH

def handle_events(ambulance):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ambulance.move("left")
    if keys[pygame.K_RIGHT]:
        ambulance.move("right")
    if keys[pygame.K_UP]:
        ambulance.move("up")
    if keys[pygame.K_DOWN]:
        ambulance.move("down")
    return True

def check_collision(ambulance, obstacles):
    for obstacle in obstacles:
        if ambulance.x < obstacle.x + 50 and ambulance.x + 50 > obstacle.x and ambulance.y < obstacle.y + 50 and ambulance.y + 50 > obstacle.y:
            return True
    return False

def draw_objects(screen, ambulance, obstacles, score, background_y):
     screen.fill(GREEN)
     pygame.draw.rect(screen, BLACK, (0, background_y % HEIGHT, WIDTH, HEIGHT))
     
     ambulance.draw(screen)
     
     for obstacle in obstacles:
        obstacle.draw(screen)
        
        font = pygame.font.Font(FONT_STYLE, 35)
        score_text = font.render(f"Score: " + str(score), True, BLACK)
        screen.blit(score_text, (10, 10))