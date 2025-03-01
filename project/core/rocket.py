import pygame as pg
from core import environment
from core.base_object import Base_Rectangle
import physics_engine
import numpy as np
import math


    
class Rocket(Base_Rectangle):
    def __init__(self,screen,launchsite,result = None,object_type = "rocket",dt=None,x=None,y=None,width=40,height=80):
        self.original_image = pg.image.load('linked_files/rocket-147466_960_720.png')
        self.original_image = pg.transform.scale(self.original_image, (50, 100))
        self.image = self.original_image.copy()
        self.image = pg.transform.rotate(self.image, 0)#self.tilt)
        image_rect = self.image.get_rect()
        
        self.result = result
        self.height = image_rect.height
        self.width = image_rect.width
        
        self.screen = screen

        self.x = launchsite.x+launchsite.width*.5-self.width*.5
        self.y = launchsite.y-self.height
        self.dt = dt
        
        #TESING INITIAL MASS, THRUST & ANGLE
        self.mass = 10                      #EXAMPLE mass of rocket (kg)
        self.thrust = 0                   #EXAMPLE initial thrust (N)
        self.angle = np.radians(90)         #EXAMPLE initial angle of rocket (rad)
        self.velocity = [0,0]

        # Add this line to define is_thrusting
        self.is_thrusting = False  # Tracks whether thrust is active


    def draw(self):
        
        image = self.original_image
        #image = self.original_image if self.vy >=0 else pg.transform.rotate(self.original_image, 180)
        image_rect = image.get_rect()
        image_rect.center = (self.x+self.width/2,self.y+self.height/2)
            
        pg.draw.rect(self.screen,"red",(self.x,self.y,self.width,self.height))
        self.screen.blit(image, image_rect)

    def erase(self):
        pass

    def compute_altitude(self):
        return max(0, self.launchsite.y - self.y)

    def check_collision(self,other,environment):
        pass
        
    

    def update(self, environment=None):
    
        # Calculate the magnitude of thrust components
        self.thrust_x = self.thrust * np.cos(self.angle)
        self.thrust_y = self.thrust * np.sin(self.angle)

        # Calculate force
        self.force_x = self.thrust_x
        self.force_y = self.thrust_y + (self.mass * environment.gravity)  # Inverted for pygame coordinates
        self.force = np.array([self.force_x, self.force_y])

        # Use physics_engine to calculate acceleration
        self.acceleration = physics_engine.calculate_acceleration(self.force, self.mass)

        if self.is_thrusting:  # Apply thrust only when 'W' is pressed
            self.thrust_x = self.thrust * np.cos(self.angle)
            self.thrust_y = self.thrust * np.sin(self.angle)

            self.force_x = self.thrust_x
            self.force_y = self.thrust_y + (self.mass * environment.gravity)  # Gravity included

            self.force = np.array([self.force_x, self.force_y])
            self.acceleration = physics_engine.calculate_acceleration(self.force, self.mass)

            self.launch()  # Apply physics to move the rocket

    def launch(self):
        
        # Update velocity
        self.velocity = np.array(self.velocity) + (np.array(self.acceleration) * self.dt)

        # Update position
        self.x += self.velocity[0] * self.dt
        self.y -= self.velocity[1] * self.dt  # Inverted for pygame coordinates

        print(f"Thrust: {self.thrust_y}, Force: {self.force_y}, Velocity: {self.velocity}, Position: ({self.x}, {self.y})")

        