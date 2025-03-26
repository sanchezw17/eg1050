import pygame as pg
import numpy as np
from core.base_object import Base_object

class Asteroid(Base_object):
    def __init__(self, screen, x=None, y=None, radius=20, speed=2):
        super().__init__(screen, object_type="Asteroid", mass=1, static=False, x=x, y=y)
        self.radius = radius
        self.speed = speed
        self.vx = np.random.uniform(-1, 1) * self.speed
        self.vy = np.random.uniform(-1, 1) * self.speed

    def draw(self):
        pg.draw.circle(self.screen, "gray", (int(self.x), int(self.y)), self.radius)

    def update_position(self):
        self.x += self.vx
        self.y += self.vy

    def check_boundary(self):
        if self.x + self.radius > self.screen.get_width() or self.x - self.radius < 0:
            self.vx = -self.vx
        if self.y + self.radius > self.screen.get_height() or self.y - self.radius < 0:
            self.vy = -self.vy

    def check_collision(self, rocket):
        distance = np.sqrt((self.x - rocket.x_pos)**2 + (self.y - rocket.y_pos)**2)
        if distance < self.radius + rocket.width / 2:
            return True
        return False