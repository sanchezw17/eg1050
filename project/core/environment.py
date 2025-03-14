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

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Collecting Gold Coins")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)  # Gold color for the coin
LIGHT_YELLOW = (255, 255, 150)  # Shiny highlight

# Load rocket image
rocket_img = pygame.image.load("rocket.png")  # Ensure you have a rocket image
rocket_img = pygame.transform.scale(rocket_img, (50, 80))

# Load sound
coin_sound = pygame.mixer.Sound("coin_sound.wav")  # Ensure you have a coin sound file

# Rocket settings
rocket_x, rocket_y = WIDTH // 2, HEIGHT - 100
rocket_speed = 5

# Coin settings
coin_x, coin_y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
coin_collected = 0
coin_radius = 15  # Size of the gold coin

# Font for coin counter
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)  # Background color

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rocket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rocket_x > 0:
        rocket_x -= rocket_speed
    if keys[pygame.K_RIGHT] and rocket_x < WIDTH - 50:
        rocket_x += rocket_speed
    if keys[pygame.K_UP] and rocket_y > 0:
        rocket_y -= rocket_speed
    if keys[pygame.K_DOWN] and rocket_y < HEIGHT - 80:
        rocket_y += rocket_speed

    # Collision detection (if rocket touches coin)
    rocket_rect = pygame.Rect(rocket_x, rocket_y, 50, 80)
    coin_rect = pygame.Rect(coin_x - coin_radius, coin_y - coin_radius, coin_radius * 2, coin_radius * 2)

    if rocket_rect.colliderect(coin_rect):
        coin_collected += 1
        coin_sound.play()  # Play coin collection sound
        coin_x, coin_y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)  # Spawn new coin

    # Draw rocket
    screen.blit(rocket_img, (rocket_x, rocket_y))

    # Draw gold coin
    pygame.draw.circle(screen, GOLD, (coin_x, coin_y), coin_radius)  # Main gold coin
    pygame.draw.circle(screen, LIGHT_YELLOW, (coin_x - 5, coin_y - 5), 5)  # Shiny highlight

    # Display coin counter
    coin_text = font.render(f"Coins: {coin_collected}", True, WHITE)
    screen.blit(coin_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()

