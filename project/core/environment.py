import pygame
from settings import screen, WIDTH, HEIGHT, seed

def draw_walls():
    left = pygame.draw.line(screen, "black", (0, 0), (0, HEIGHT), 10)
    right = pygame.draw.line(screen, "black", (WIDTH, 0), (WIDTH, HEIGHT), 10)
    top = pygame.draw.line(screen, "black", (0, 0), (WIDTH, 0), 10)
    bottom = pygame.draw.line(screen, "black", (0, HEIGHT), (WIDTH, HEIGHT), 10)
    walls = [left, right, top, bottom]
    return walls

def make_environment(WIDTH, HEIGHT, seed):
    # Create starting pad
    pygame.draw.rect(screen, "darkgrey", (0, HEIGHT - 80, 100, 80))
    block_start = pygame.Rect(0, HEIGHT - 80, 100, 80)

    # Create ending pad
    pygame.draw.rect(screen, "darkgrey", (WIDTH - 100, HEIGHT - 80, 100, 80))
    block_end = pygame.Rect(WIDTH - 100, HEIGHT - 80, 100, 80)

    # Create block for each square, using random game variables
    block_2 = pygame.Rect(100, HEIGHT - seed[0], 100, seed[0])
    pygame.draw.rect(screen, "white", block_2)

    block_3 = pygame.Rect(200, HEIGHT - seed[1], 100, seed[1])
    pygame.draw.rect(screen, "white", block_3)

    block_4 = pygame.Rect(300, HEIGHT - seed[2], 100, seed[2])
    pygame.draw.rect(screen, "white", block_4)

    block_5 = pygame.Rect(400, HEIGHT - seed[3], 100, seed[3])
    pygame.draw.rect(screen, "white", block_5)

    block_6 = pygame.Rect(500, HEIGHT - seed[4], 100, seed[4])
    pygame.draw.rect(screen, "white", block_6)

    block_7 = pygame.Rect(600, HEIGHT - seed[5], 100, seed[5])
    pygame.draw.rect(screen, "white", block_7)

    block_8 = pygame.Rect(700, HEIGHT - seed[6], 100, seed[6])
    pygame.draw.rect(screen, "white", block_8)

    block_9 = pygame.Rect(800, HEIGHT - seed[7], 100, seed[7])
    pygame.draw.rect(screen, "white", block_9)

    blocks = [block_start, block_end, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9]
    return blocks
