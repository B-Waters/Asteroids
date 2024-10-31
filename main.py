# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from shot import Shot
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid

# Base class for game objects
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #updatable.add(myPlayer)
    #drawable.add(myPlayer)

    Shot.containers = (updatable, drawable, shots)
    #Did not originally add shots to this
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    myPlayer = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")

        for x in updatable:
            x.update(dt)

        for x in asteroids:
            if x.collisions(myPlayer) == True:
                print("Game over!")
                sys.exit()
            for y in shots:
                if x.collisions(y):
                    y.kill()
                    x.split()

        for x in drawable:
            x.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
