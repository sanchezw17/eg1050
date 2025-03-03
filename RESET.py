# Example file showing a circle moving on screen
import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
timer = pygame.time.Clock()

#Game Variables
wall_thickness = 10
GRAVITY = 0.5
bounce_stop = 0.3
#track position of mouse to get movement vector
mouse_trajectory = []

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, y_speed, x_speed, id, selected = False):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id
        self.selected = selected
    
    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self):
        if not self.selected:
            if self.y_pos < HEIGHT - self.radius - (wall_thickness/2):
                self.y_speed += GRAVITY
            else:
                if self.y_speed > bounce_stop:
                    self.y_speed *= -self.retention
                else:
                    if abs(self.y_speed) < bounce_stop:
                        self.y_speed = 0
        else:
           
            
            self.y_speed = 0


    def update_position(self):
        if not self.selected:
            self.y_pos += self.y_speed
            self.x_pos += self.x_speed
            return self.y_pos, self.x_pos
        else:
            self.x_pos, self.y_pos = pygame.mouse.get_pos() 


    def check_select(self, pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected





ball1 = Ball(100, 100, 10, "yellow", 10, 0.5, 0, 0, 1)
ball2 = Ball(200, 200, 10, "black", 10, 0.5, 0, 0, 2) 

ball_list = [ball1, ball2]  



def draw_walls():
    left = pygame.draw.line(screen, "green", (0,0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, "green", (WIDTH,0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, "green", (0,0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, "green", (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list




#Game loup
run = True
while run:
    timer.tick(FPS)
    screen.fill("blue")

    ball1.draw()
    ball2.draw()
    ball1.y_speed = ball1.check_gravity()
    ball2.y_speed = ball2.check_gravity()
    ball1.update_position()
    ball2.update_position()
    walls = draw_walls()
    ball1.check_gravity()
    ball2.check_gravity()



#Getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 


        if event.type == pygame.MOUSEBUTTONDOWN:
            if ball1.check_select(event.pos) or ball2.check_select(event.pos):
                active_select = True

        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(ball_list)):
                ball_list[i].check_select((-1000,-1000))
            active_select = False

               

    pygame.display.flip()

pygame.quit()



