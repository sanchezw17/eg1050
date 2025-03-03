import pygame as pg
from core import environment
from core.base_object import Base_Rectangle
import physics_engine
import numpy as np
import math

class Rocket(Base_Rectangle):
    def __init__(self, screen, launchsite, result=None, object_type="rocket", dt=None, x=None, y=None, width=40, height=80):
        self.original_image = pg.image.load('linked_files/rocket-147466_960_720.png')
        self.original_image = pg.transform.scale(self.original_image, (50, 100))
        self.image = self.original_image.copy()
        self.angle = 90  # Initialize the angle of the rocket
        image_rect = self.image.get_rect()
        
        self.result = result
        self.height = image_rect.height
        self.width = image_rect.width
        
        self.screen = screen
        self.x = launchsite.x + launchsite.width * 0.5 - self.width * 0.5
        self.y = launchsite.y - self.height
        self.dt = dt
        
        self.mass = 10  # Example mass of rocket (kg)
        self.thrust = 0  # Example initial thrust (N)
        self.velocity = [0, 0]
        self.is_thrusting = False  # Tracks whether thrust is active

    def draw(self):
        # Rotate the image based on the angle
        rotated_image = pg.transform.rotate(self.original_image, -self.angle)
        new_rect = rotated_image.get_rect(center=self.original_image.get_rect(topleft=(self.x, self.y)).center)
        self.screen.blit(rotated_image, new_rect.topleft)

    def erase(self):
        pass

    def compute_altitude(self):
        return max(0, self.launchsite.y - self.y)

    def check_collision(self, other, environment):
        pass

    def update(self, environment=None):
        thrust_x = self.thrust * np.cos(np.radians(self.angle))
        thrust_y = self.thrust * np.sin(np.radians(self.angle))

        force_x = thrust_x
        force_y = thrust_y + (self.mass * environment.gravity)
        force = np.array([force_x, force_y])

        acceleration = physics_engine.calculate_acceleration(force, self.mass)

        if self.is_thrusting:
            self.thrust_x = self.thrust * np.cos(np.radians(self.angle))
            self.thrust_y = self.thrust * np.sin(np.radians(self.angle))

            self.force_x = self.thrust_x
            self.force_y = self.thrust_y + (self.mass * environment.gravity)

            self.force = np.array([self.force_x, self.force_y])
            self.acceleration = physics_engine.calculate_acceleration(self.force, self.mass)

            self.launch()

        self.angle = self.calculate_angle()

    def launch(self):
        self.velocity = np.array(self.velocity) + (np.array(self.acceleration) * self.dt)
        self.x += self.velocity[0] * self.dt
        self.y -= self.velocity[1] * self.dt

    def calculate_angle(self):
        return np.degrees(np.arctan2(-self.velocity[1], self.velocity[0]))

    def thrust(self, force):
        self.velocity[0] += force * np.cos(np.radians(self.angle))
        self.velocity[1] += force * np.sin(np.radians(self.angle))




