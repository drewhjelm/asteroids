import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    #return "'Starting asteroids!'"
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #pygame.Surface.fill(screen, (255,255,255))

    clock = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()

    Player.containers = (group_drawable,group_updatable)

    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
    AsteroidField.containers = group_updatable

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        keys = pygame.key.get_pressed()
        for obj in group_updatable:
            obj.update(dt)
        
        screen.fill("black")

        for obj in group_drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        tock = clock.tick(60)
        dt += tock/1000

if __name__ == "__main__":
    main()