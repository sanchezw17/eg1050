import numpy as np
import pygame

pygame.init()
pygame.mixer.init()

# Screen settings
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game settings
fps = 60
timer = pygame.time.Clock()
GRAVITY = 0.15
THRUST = 0.2
TURN_AMOUNT = 0.87
seed = np.random.randint(0, 350, 9)

seed[seed < 100] = abs(seed[seed<100])

# Load assets
background_image = pygame.image.load("project/linked_files/png/backgroundimage.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
sun_image = pygame.image.load("project/linked_files/png/GOATV6.png")
sun_image = pygame.transform.scale(sun_image, (200, 200))
engine_sound = pygame.mixer.Sound("project/linked_files/audio/engine_sound.mp3")
engine_sound.set_volume(0.2)