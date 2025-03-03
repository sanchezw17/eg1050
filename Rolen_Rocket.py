
import pygame
import numpy as np

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
timer = pygame.time.Clock()

#Game Variables
wall_thickness = 10
GRAVITY = 0.5
bounce_stop = 0.3

class Rocket:
    def __init__(self, x_pos, y_pos, width, height, color, mass, y_speed, x_speed, y_accel, x_accel, resistance, angle, id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
    
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.y_accel = y_accel
        self.x_accel = x_accel
        self.resistance = resistance
        self.angle = angle
        self.id = id
       
    
    def draw(self):
        self.rect = pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos), self.width, self.height)


rocket_1 = Rocket(100, 100, 10, "yellow", 10, 0.5, 0, 0, 1, 1, 0.3, 0, 1)   

def draw_walls():
    left = pygame.draw.line(screen, "green", (0,0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, "green", (WIDTH,0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, "green", (0,0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, "green", (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list




#Game loup
run = True
while run:
    timer.tick(FPS)
    screen.fill("blue")
    draw_walls()
    rocket_1.draw()
    


#Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 



               

    pygame.display.flip()

pygame.quit()# Example file showing a circle moving on screen
import pygame



