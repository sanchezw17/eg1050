import pygame
from settings import *
from core.utils import *
from core.rocket import Rocket
from core.environment import draw_walls, make_environment, generate_coins

rocket = Rocket(25, HEIGHT - 180, 100, 50, "red", 1, 0, 0, 0, 0, np.pi / 2, 0)

font = pygame.font.Font(None, 36)  # Choose a font and size

# Load coin image directly in main.py
coin_img = pygame.image.load("project/linked_files/png/b_bitcoin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Generating Coins More Coins Better desc
coins, coins_img = generate_coins()

run = True
while run:
    timer.tick(fps)
    screen.blit(background_image, (0, 0))
    screen.blit(sun_image, (WIDTH - 200, 0))
    walls = draw_walls()
    rocket.draw()
    rocket.update_forces()
    rocket.update_acceleration()
    rocket.check_collision()
    rocket.update_speed()
    rocket.update_position()
    rocket.print_info()
    blocks = make_environment(WIDTH, HEIGHT, seed)
    rocket.check_collision_blocks(blocks)

    # In the game loop, after drawing everything else
    score_text = font.render(f"Score: {rocket.score}", True, (255, 255, 255))  # White text
    screen.blit(score_text, (10, 10))  # Display at the top-left corner

    # Check for collisions with coins
    rocket.check_collision_coins(coins)

    # Draw coins
    for coin_pos in coins:
        screen.blit(coin_img, coin_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Handle key releases (stop thrust when keys are released)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rocket.thrust = 0
                engine_sound.fadeout(250)
            if event.key == pygame.K_s:
                rocket.thrust = 0

    # Handle continuous key presses for rotation and thrust
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Rotate counterclockwise (left)
        rocket.angle += np.radians(TURN_AMOUNT)  # Increase angle
    if keys[pygame.K_d]:  # Rotate clockwise (right)
        rocket.angle -= np.radians(TURN_AMOUNT)  # Decrease angle
    if keys[pygame.K_w]:  # Thrust forward
        rocket.thrust = THRUST
        if not pygame.mixer.get_busy():  # Play only if not already playing
            engine_sound.play(-1)  # Loop the engine sound
    if keys[pygame.K_s]:  # Thrust backward
        rocket.thrust = -THRUST

    pygame.display.flip()

pygame.quit()
