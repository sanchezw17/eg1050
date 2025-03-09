import pygame
import numpy as np

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps = 60
timer = pygame.time.Clock()

# Game variables
GRAVITY = 0.15
THRUST = 0.2
TURN_AMOUNT = 5
seed = np.random.randint(0, 250, 9)

# Makes seed be 0 more often
for i in range(len(seed)):
    if seed[i] < 100:
        seed[i] = 0

# Make rocket (rectangle)
class Rocket:
    def __init__(self, x_pos, y_pos, height, width, color, mass, x_speed, y_speed, x_acceleration, y_acceleration, angle, thrust):
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

    # draw the rocket
    def draw(self):
        rocket = pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))
        return rocket

    def update_forces(self):
        # update forces
        self.y_force = self.mass * GRAVITY - self.thrust * np.sin(self.angle)
        self.x_force = self.thrust * np.cos(self.angle)

        return self.x_force, self.y_force

    def update_acceleration(self):
        # update acceleration based on forces
        self.y_acceleration = self.y_force / self.mass
        self.x_acceleration = self.x_force / self.mass

        return self.y_acceleration, self.x_acceleration

    def update_speed(self):
        # updates speed based on the acceleration
        self.y_speed += self.y_acceleration
        self.x_speed += self.x_acceleration

        return self.x_speed, self.y_speed

    # update position of rocket based on speed
    def update_position(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    # Checks collision KEEP IN MIND POSITION OF RECTANGLE IS TOP LEFT CORNER OF IT
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

    # Check collision with blocks
    def check_collision_blocks(self, blocks):
        rocket_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        for block in blocks:
            if rocket_rect.colliderect(block):
                # Stop the rocket's speed immediately and adjust its position
                if self.y_pos + self.height <= block.top + self.y_speed:  # Collision from top
                    self.y_speed = 0  # Stop vertical movement
                    self.y_pos = block.top - self.height  # Position it on top of the block
                elif self.y_pos >= block.bottom + self.y_speed:  # Collision from bottom
                    self.y_speed = 0  # Stop vertical movement
                    self.y_pos = block.bottom  # Position it at the bottom of the block

                if self.x_pos + self.width <= block.left + self.x_speed:  # Collision from left
                    self.x_speed = 0  # Stop horizontal movement
                    self.x_pos = block.left - self.width  # Position it to the left of the block
                elif self.x_pos >= block.right + self.x_speed:  # Collision from right
                    self.x_speed = 0  # Stop horizontal movement
                    self.x_pos = block.right  # Position it to the right of the block

                # Adjust rocket's position to avoid overlap if it's already inside a block.
                # Prevent the rocket from "sliding" through the block after a collision.
                if self.x_pos < block.left:
                    self.x_pos = block.left - self.width
                if self.x_pos + self.width > block.right:
                    self.x_pos = block.right
                if self.y_pos < block.top:
                    self.y_pos = block.top - self.height
                if self.y_pos + self.height > block.bottom:
                    self.y_pos = block.bottom

    def print_info(self):
        print(f"x_pos:{self.x_pos}, y_pos:{self.y_pos}, x_speed:{self.x_speed}, y_speed: {self.y_speed}, x_acceleration: {self.x_acceleration}, y_acceleration: {self.y_acceleration}, angle: {self.angle}, thrust: {self.thrust}")

# Make walls
def draw_walls():
    left = pygame.draw.line(screen, "green", (0, 0), (0, HEIGHT), 10)
    right = pygame.draw.line(screen, "green", (WIDTH, 0), (WIDTH, HEIGHT), 10)
    top = pygame.draw.line(screen, "green", (0, 0), (WIDTH, 0), 10)
    bottom = pygame.draw.line(screen, "black", (0, HEIGHT), (WIDTH, HEIGHT), 10)
    walls = [left, right, top, bottom]
    return walls

# Make procedural environment
def make_environment(WIDTH, HEIGHT, seed):
    # Create starting pad
    block_start = pygame.Rect(0, HEIGHT - 80, 100, 80)

    # Create ending pad
    block_end = pygame.Rect(WIDTH - 100, HEIGHT - 80, 100, 80)

    # Create blocks for each square, using random game variables
    blocks = [
        block_start,
        block_end,
        pygame.Rect(100, HEIGHT - seed[0], 100, seed[0]),
        pygame.Rect(200, HEIGHT - seed[1], 100, seed[1]),
        pygame.Rect(300, HEIGHT - seed[2], 100, seed[2]),
        pygame.Rect(400, HEIGHT - seed[3], 100, seed[3]),
        pygame.Rect(500, HEIGHT - seed[4], 100, seed[4]),
        pygame.Rect(600, HEIGHT - seed[5], 100, seed[5]),
        pygame.Rect(700, HEIGHT - seed[6], 100, seed[6]),
        pygame.Rect(800, HEIGHT - seed[7], 100, seed[7])
    ]

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(screen, "green", block)

    return blocks

# Create rocket for the game
rocket1 = Rocket(50, HEIGHT - 180, 100, 50, "red", 1, 0, 0, 0, 0, np.pi / 2, 0)

# Main Game loop
run = True
while run:
    timer.tick(fps)
    screen.fill("blue")
    walls = draw_walls()
    rocket1.draw()
    rocket1.update_forces()
    rocket1.update_acceleration()
    rocket1.check_collision()
    blocks = make_environment(WIDTH, HEIGHT, seed)  # Get the blocks
    rocket1.check_collision_blocks(blocks)  # Pass blocks for collision detection
    rocket1.update_speed()
    rocket1.update_position()
    rocket1.print_info()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Make the rocket move
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()  # Get currently pressed keys
            if keys[pygame.K_w]:
                rocket1.thrust = THRUST
            if keys[pygame.K_s]:
                rocket1.thrust = -THRUST
            if keys[pygame.K_a]:
                rocket1.angle += np.radians(TURN_AMOUNT)
            if keys[pygame.K_d]:
                rocket1.angle -= np.radians(TURN_AMOUNT)

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                rocket1.thrust = 0  # Stop thrust when releasing keys

    pygame.display.flip()
pygame.quit()
