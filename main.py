# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    player = Player(x,y)
    asteroidfield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)

        for c in asteroids:
            if c.collisions(player):
                print("Game over!")
                sys.exit()

        for o in drawable:
            o.draw(screen)
        
        pygame.display.flip()
        
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()