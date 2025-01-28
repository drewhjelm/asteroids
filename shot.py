from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen,"red",self.position,self.radius,2)

    def update(self, dt):  
        self.position += (self.velocity * dt)/50