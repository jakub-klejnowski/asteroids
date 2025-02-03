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
    Shot.containers = (shots, updatable, drawable)

    player = Player(x,y)
    asteroidfield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatable.update(dt)

        for a in asteroids:
            if a.collisions(player):
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.collisions(s):
                    s.kill()
                    a.split()

        screen.fill("black") 

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()