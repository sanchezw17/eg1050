import pygame
import numpy as np
from settings import screen, WIDTH, HEIGHT, background_image, engine_sound, max_fuel
def show_you_win_screen():
    win_img = pygame.image.load("project/linked_files/png/Hell v2.jpg")
    win_img = pygame.transform.scale(win_img, (WIDTH, HEIGHT))
    win_sound = pygame.mixer.Sound("project/linked_files/audio/Boom._boom.wav.wav")
    win_sound.play()
    screen.blit(win_img, (0, 0))

    pygame.display.flip()
    pygame.time.delay(10000)

def show_you_died_screen():
    engine_sound.stop()  # Stop the engine sound when the rocket explodes
    you_died_img = pygame.image.load("project/linked_files/png/you_died.jpeg")  # Load the image
    you_died_img = pygame.transform.scale(you_died_img, (WIDTH, HEIGHT))  # Scale to fullscreen
    screen.blit(you_died_img, (0, 0))  # Draw image covering the screen

    # Load and play the death sound
    death_sound = pygame.mixer.Sound("project/linked_files/audio/death_sound.wav")  # Replace with the actual sound file path
    death_sound.set_volume(1.0)
    death_sound.play()

    pygame.display.flip()  # Update the screen
    pygame.time.delay(5500)

def show_explosion(rocket):
    # Load explosion sound
    explosion_sound = pygame.mixer.Sound("project/linked_files/audio/explosion_sound.wav")  # Ensure you have the sound file
    explosion_sound.set_volume(0.1)
    # Play the explosion sound
    explosion_sound.play()  # Play the explosion sound when the explosion happens

    # Load explosion image
    explosion_img = pygame.image.load("project/linked_files/png/explosion.png")
    explosion_img = pygame.transform.scale(explosion_img, (50, 50))  # Initial size of explosion

    # Animate explosion from small to big
    explosion_size = 50  # Initial size
    max_size = 500  # Maximum size of explosion
    scale_step = 50  # How much the explosion grows every frame
    duration = 10  # Number of frames the explosion lasts

    for i in range(duration):
        screen.blit(background_image, (0, 0))  # Clear the screen (for each frame)
        # Draw other game elements here (rocket, blocks, etc.)
        rocket.draw()  # Draw rocket

        # Update explosion size (grow it over time)
        explosion_size += scale_step
        if explosion_size > max_size:
            explosion_size = max_size  # Limit the maximum size

        # Calculate the position to center the explosion on the rocket
        explosion_x = rocket.x_pos + rocket.width // 2 - explosion_size // 2
        explosion_y = rocket.y_pos + rocket.height // 2 - explosion_size // 2

        # Resize the explosion image to the new size
        scaled_explosion = pygame.transform.scale(explosion_img, (explosion_size, explosion_size))
        screen.blit(scaled_explosion, (explosion_x, explosion_y))  # Draw explosion centered on rocket

        pygame.display.flip()  # Update display
        pygame.time.delay(50)  # Delay to animate explosion (adjust for speed)

    # After explosion animation, show "You Died" screen
    show_you_died_screen()

def reset_game(rocket, seed):
    # Reset rocket attributes
    rocket.x_pos = 25
    rocket.y_pos = HEIGHT - 180
    rocket.x_speed = 0
    rocket.y_speed = 0
    rocket.x_acceleration = 0
    rocket.y_acceleration = 0
    rocket.angle = np.pi / 2
    rocket.thrust = 0
    rocket.fuel = max_fuel
    rocket.score = 0

    seed[:] = np.random.randint(0, 250, 9)  # Generate new terrain

import random

# Asteroid setup
asteroids = [pygame.Rect(random.randint(0, 750), random.randint(-600, -50), 50, 50) for _ in range(5)]
asteroid_speed = 3

# Load Images
you_died_img = pygame.image.load("project/linked_files/png/you_died.jpeg")  
asteroid_img = pygame.image.load("project/linked_files/png/asteroid.png")  

def move_asteroids():
    for asteroid in asteroids:
        asteroid.y += asteroid_speed
        if asteroid.y > 600:  # Reset asteroid to top when it leaves screen
            asteroid.y = random.randint(-600, -50)
            asteroid.x = random.randint(0, 750)

def draw_asteroids(screen):
    for asteroid in asteroids:
        screen.blit(asteroid_img, (asteroid.x, asteroid.y))  

def check_collision(player, screen):
    for asteroid in asteroids:
        if player.colliderect(asteroid):
            engine_sound.stop()  # Stop the engine sound when the rocket explodes
            you_died_img = pygame.image.load("project/linked_files/png/you_died.jpeg")  # Load the image
            you_died_img = pygame.transform.scale(you_died_img, (WIDTH, HEIGHT))  # Scale to fullscreen
            screen.blit(you_died_img, (0, 0))  # Draw image covering the screen

            # Load and play the death sound
            death_sound = pygame.mixer.Sound("project/linked_files/audio/death_sound.wav")  # Replace with the actual sound file path
            death_sound.set_volume(1.0)
            death_sound.play()

            pygame.display.flip()  # Update the screen
            pygame.time.delay(5500)