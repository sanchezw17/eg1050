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
                event.keys = pg.key.get_pressed()
                if event.keys[pygame.K_w]:
                    rocket.thrust += 5
                if event.keys[pygame.K_s]:
                   rocket.thrust -= 10
                if event.keys[pygame.K_a]:
                    rocket.angle += 10
                if event.keys[pygame.K_d]:
                    rocket.angle -= 10
                if event.keys[pygame.K_SPACE]:
                    rocket.fire()
            

                          
        
        #in games you should draw/delete the objects in the environment each frame elsewise shapes bleed together for moving objects
        env.draw_objects()
        rocket.draw()

        rocket.erase()        
        rocket.dt = dt
    
    #This is where you would handle the physics of the rocket
    #Also update rockets
        rocket.check_boundary(env)
        #[rocket.check_collision(obj) for obj in env.objects]
        rocket.update(env)
    
    #redraw the rocket
        rocket.draw()

    #update screen and dt
        time_elapsed += dt
        pg.display.flip()
     
    pg.quit()

if __name__ == "__main__":
    main()