import pygame
import random
from settings import screen, WIDTH, HEIGHT, seed

def draw_walls():
    left = pygame.draw.line(screen, "black", (0, 0), (0, HEIGHT), 10)
    right = pygame.draw.line(screen, "black", (WIDTH, 0), (WIDTH, HEIGHT), 10)
    top = pygame.draw.line(screen, "black", (0, 0), (WIDTH, 0), 10)
    bottom = pygame.draw.line(screen, "black", (0, HEIGHT), (WIDTH, HEIGHT), 10)
    walls = [left, right, top, bottom]
    return walls

endstone = pygame.image.load("project/linked_files/png/end_stone.jpg").convert_alpha()

endstone = pygame.transform.scale(endstone, (100, 80))

def make_environment(WIDTH, HEIGHT, seed):
    # Create starting pad
    pygame.draw.rect(screen, "darkgrey", (0, HEIGHT - 80, 100, 80))
    block_start = pygame.Rect(0, HEIGHT - 80, 100, 80)

    # Create ending pad
    pygame.draw.rect(screen, "darkgrey", (WIDTH - 100, HEIGHT - 80, 100, 80))
    block_end = pygame.Rect(WIDTH - 100, HEIGHT - 80, 100, 80)

    # Create block for each square, using random game variables
    blocks = [block_start, block_end]
    for i in range(1,9):
        block_height = seed[i-1]
        block_rect = pygame.Rect(100 * (i), HEIGHT - block_height, 100, block_height)


        for x in range(block_rect.left, block_rect.right, endstone.get_width()):
            for y in range(block_rect.top, block_rect.bottom, endstone.get_height()):
                screen.blit(endstone, (x, y))

        blocks.append(block_rect)

    return blocks