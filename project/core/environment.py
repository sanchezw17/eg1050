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

coin_img = pygame.image.load("project/linked_files/png/Bitcoin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

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

# Make a func for coins
def generate_coins():
    coins = []
    num_coins = random.randint(3, 5)  # Randomly choose between 3 to 5 coins
    for _ in range(num_coins):
        # Randomly place the coin near the top of the screen
        coin_x = random.randint(50, WIDTH - 50)  # Avoid spawning too close to the edges
        coin_y = random.randint(50, 200)  # Spawn near the top of the screen
        coins.append((coin_x, coin_y))
    return coins, coin_img
