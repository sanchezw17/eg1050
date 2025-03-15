import pygame
from settings import *
from core.utils import *
from core.rocket import Rocket
from core.environment import draw_walls, make_environment

rocket = Rocket(25, HEIGHT - 180, 100, 50, "red", 1, 0, 0, 0, 0, np.pi / 2, 0)

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
