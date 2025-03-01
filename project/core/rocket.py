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
        

    def update(self,environment=None):

        #EXAMPLE Calculate the magnitude of thrust components
        thrust_x = self.thrust * np.cos(self.angle)
        thrust_y = self.thrust * np.sin(self.angle)

        #EXAMPLE Calculate force
        force_x = thrust_x
        force_y = thrust_y + (self.mass * environment.gravity) #inverted for pygame coordinates (0,0) at the top left
        force = np.array([force_x, force_y])

        #Use physics_engine to calculate acceleration with force and mass
        acceleration = physics_engine.calculate_acceleration(force,self.mass)

        #Update velocity 
        # a = dv/dt
        # a * dt = vf - vi
        # vf = vi + (a * dt) 
        self.velocity = np.array(self.velocity) + (np.array(acceleration) * self.dt)
        
        # v = ds/dt
        # v * dt = sf - si
        # sf = si + (v * dt) 
        self.x += self.velocity[0] * self.dt
        self.y -= self.velocity[1] * self.dt        #inverted for pygame coordinates (0,0) at the top left
        print(f"Thrust: {thrust_y} Force: {force_y} Velocity: {self.velocity}, Position: ({self.x}, {self.y})")
        #this will update forces and stuff 



 