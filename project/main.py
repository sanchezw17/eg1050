import pygame
from settings import *
from core.utils import *
from core.rocket import Rocket
from core.asteroids import Asteroid
from core.environment import draw_walls, make_environment

rocket = Rocket(25, HEIGHT - 180, 100, 50, "red", 1, 0, 0, 0, 0, np.pi / 2, 0, 100)
asteroids = [Asteroid(screen, x=np.random.randint(0, WIDTH), y=np.random.randint(0, HEIGHT), speed=np.random.uniform(1, 3)) for _ in range(10)]

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
    rocket.update_fuel()
    blocks = make_environment(WIDTH, HEIGHT, seed)
    rocket.check_collision_blocks(blocks)

    for asteroid in asteroids:
        asteroid.draw()

    for asteroid in asteroids:
        asteroid.update_position()
        asteroid.check_boundary()
        if asteroid.check_collision(rocket):
            show_explosion(rocket)
            reset_game(rocket, seed)
              
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Handle key releases (stop thrust when keys are released)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rocket.thrust = 0
                engine_sound.fadeout(250)

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

    # Draw fuel guage
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 200, 20))
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, rocket.fuel * 4, 20))

    # Display fuel level as text
    fuel_test = fuel_font.render(f"Fuel: {int(rocket.fuel)}%", True, (255, 255, 255))
    screen.blit(fuel_test, (10, 40))

    pygame.display.flip()

pygame.quit()
