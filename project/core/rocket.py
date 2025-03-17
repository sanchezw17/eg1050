import pygame
import numpy as np
from settings import screen, WIDTH, HEIGHT, GRAVITY, seed, max_fuel, fuel_consumption_rate
from core.utils import show_you_win_screen, show_explosion, reset_game, coins

class Rocket:
    def __init__(self, x_pos, y_pos, height, width, color, mass, x_speed, y_speed, x_acceleration, y_acceleration, angle, thrust, fuel):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.color = color
        self.mass = mass
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_acceleration = x_acceleration
        self.y_acceleration = y_acceleration
        self.angle = angle
        self.thrust = thrust
        self.fuel = max_fuel
        self.fuel = min(fuel, max_fuel)

        self.image = pygame.image.load("project/linked_files/png/rocket-147466_960_720.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, 180)
        self.flame = pygame.image.load("project/linked_files/png/rocket-thrust-1.png").convert_alpha()
        self.flame = pygame.transform.scale(self.flame, (width, 50))

        self.score = 0  # Add a score variable to track collected coins
        self.shield_strength = 1  # Shield activates for the first collision
        self.shield_image = pygame.image.load("project/linked_files/png/shield.png").convert_alpha()
        self.shield_image = pygame.transform.scale(self.shield_image, (width + 20, height + 20))  # Slightly larger than rocket

    def draw(self):
        # Rotate the rocket image
        rotated_rocket = pygame.transform.rotate(self.image, np.degrees(self.angle) + 90)
        rotated_rect = rotated_rocket.get_rect(center=(self.x_pos + self.width // 2, self.y_pos + self.height // 2))
        screen.blit(rotated_rocket, rotated_rect.topleft)

        # Draw flame if thrust is active
        if self.thrust > 0:
            # Pre-rotate the flame sprite to align it with the rocket's starting orientation
            pre_rotated_flame = pygame.transform.rotate(self.flame, -90)  # Rotate -90 degrees to align correctly

            # Rotate the pre-rotated flame to match the rocket's current angle
            rotated_flame = pygame.transform.rotate(pre_rotated_flame, np.degrees(self.angle))

            # Calculate flame offset based on the rocket's angle
            angle_rad = self.angle  # Rocket's angle in radians

            # Flame should point in the opposite direction of the rocket's nose
            # Use a fixed distance for the flame's offset
            flame_distance = self.height * 0.6  # Fixed distance from the rocket's center
            flame_offset_x = -np.cos(angle_rad) * flame_distance  # Horizontal offset
            flame_offset_y = np.sin(angle_rad) * flame_distance   # Vertical offset

            # Calculate flame position
            flame_rect = rotated_flame.get_rect(center=(
                self.x_pos + flame_offset_x + self.width // 2,  # Center horizontally
                self.y_pos + flame_offset_y + self.height // 2  # Center vertically
            ))

            screen.blit(rotated_flame, flame_rect.topleft)

        # Draw shield if active
        if self.shield_strength > 0:
            # Rotate the shield image to match the rocket's angle
            rotated_shield = pygame.transform.rotate(self.shield_image, np.degrees(self.angle) + 90)
            shield_rect = rotated_shield.get_rect(center=(self.x_pos + self.width // 2, self.y_pos + self.height // 2))
            screen.blit(rotated_shield, shield_rect.topleft)

    def update_forces(self):
        # Update forces
        self.y_force = self.mass * GRAVITY - self.thrust * np.sin(self.angle)
        self.x_force = self.thrust * np.cos(self.angle)
        return self.x_force, self.y_force

    def update_acceleration(self):
        # Update acceleration based on forces
        self.y_acceleration = self.y_force / self.mass
        self.x_acceleration = self.x_force / self.mass
        return self.y_acceleration, self.x_acceleration

    def update_speed(self):
        # Updates speed based on the acceleration
        self.y_speed += self.y_acceleration
        self.x_speed += self.x_acceleration
        return self.x_speed, self.y_speed

    def update_position(self):
        # Update position of rocket based on speed
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def update_fuel(self):
        if self.thrust > 0:
            self.fuel -= fuel_consumption_rate

        if self.fuel < 0:
            self.fuel = 0
            show_explosion(self)
            reset_game(self,seed)

    def check_collision(self):
        if self.x_pos < 0:
            self.x_pos = 0
            self.x_speed = 0
        if self.x_pos > WIDTH - self.width:
            self.x_pos = WIDTH - self.width
            self.x_speed = 0
        if self.y_pos < 0:
            self.y_pos = 0
            self.y_speed = 0
        if self.y_pos > HEIGHT - self.height:
            self.y_pos = HEIGHT - self.height
            self.y_speed = 0

    def check_collision_blocks(self, blocks):
        rocket_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        # The first two blocks in `blocks` are the start and end pads
        start_pad, end_pad = blocks[0], blocks[1]

        for block in blocks:
            if rocket_rect.colliderect(block):
                # If the rocket is on the start or end pad, allow it to land safely
                if block == start_pad or block == end_pad:
                    self.y_speed = 0
                    self.y_pos = block.top - self.height  # Place rocket on top

                    # Check if it's the end pad (win condition)
                    if block == end_pad:
                        show_you_win_screen()  # Show "You Win" screen
                        reset_game(self,seed,coins)  # Reset the game after winning
                else:
                    # Collision with terrain → handle shield logic
                    if self.shield_strength > 0:
                        self.shield_strength -= 1  # Reduce shield strength
                        print(f"Shield hit! Remaining shields: {self.shield_strength}")

                        # Bounce the rocket
                        self.y_speed = -self.y_speed * 0.8  # Reverse direction and reduce speed
                        self.y_pos = block.top - self.height  # Move rocket above the block

                        return  # Exit after handling the first collision
                    else:
                        # No shield → explode immediately
                        print("No shield left! Rocket explodes.")
                        show_explosion(self)
                        reset_game(self, seed)
                return  # Exit after handling the first collision

    def check_coin_collision(self, coins):
        for coin_x, coin_y in coins:
            coin_rect = pygame.Rect(coin_x, coin_y, 30, 30)  # Create coin's hitbox
            rocket_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)  # Rocket's bounding box
            if rocket_rect.colliderect(coin_rect):  # Check collision
                coin_sound.play()  # Play sound when collected
                coins.remove((coin_x, coin_y)) # Remove the coin
                self.score += 1 # Increment the score
            
coin_sound = pygame.mixer.Sound("project/linked_files/audio/mario.mp3")


