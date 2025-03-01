import core.environment
import core.projectile
import pygame as pg
import settings
import core 
from core import environment
from core.rocket import Rocket
import pygame


def is_complete():
    if Rocket.result:
        return True
    
def flight_controls(Rocket,end):

    pass

def main():

    #Boilerplate code
    pg.init()
    screen = pg.display.set_mode((1280,720))
    screen.fill((135, 206, 235))
    bckgd = pg.Surface(screen.get_size())
    bckgd.fill((135, 206, 235))
    clock = pg.time.Clock()
    running = True
    time_elapsed = 0
    
    #initialize environment
    env = environment.Environment(screen,objects=[],projectiles=[], start = core.environment.Launchpad(screen))
    env.draw_terrain(bckgd)
    rocket = Rocket(screen,env.start)
    #you can look in the code, but env.start is the start place for rocket
    while running:
        #lock framerate and get timestep
        dt = clock.tick(60)/1000
        screen.blit(bckgd, (0, 0))


        #THis handles input 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if event.key == pg.K_SPACE: # If 'space' is pressed
                    rocket.is_thrusting = True # Call the launch function
                if event.type == pg.KEYDOWN:
                    event.keys = pg.key.get_pressed()
                if event.keys[pygame.K_w]:
                    rocket.thrust += 200
                if event.keys[pygame.K_s]:
                    rocket.thrust -= 10
                if event.keys[pygame.K_a]:
                    rocket.angle += 2
                if event.keys[pygame.K_d]:
                    rocket.angle -= 2
            

        
        
        #in games you should draw/delete the objects in the environment each frame elsewise shapes bleed together for moving objects
        env.draw_objects()
        rocket.draw()

        # Update rocket and check for collisions
        rocket.erase()        
        rocket.dt = dt
    
        rocket.check_boundary(env)
        if rocket.check_collision(None, env):
            running = False  # Stop the game if collision occurs
        rocket.update(env)
    
        #redraw the rocket
        rocket.draw()

        #update screen and dt
        time_elapsed += dt
        pg.display.flip()
     
    pg.quit()

if __name__ == "__main__":
    main()