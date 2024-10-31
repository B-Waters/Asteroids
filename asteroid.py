import pygame
import random
from circleshape import CircleShape 
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        else:
            random_val =  random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            velocity1 = self.velocity.rotate(random_val)
            velocity2 = self.velocity.rotate(-random_val) 

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity2 * 1.2

            #AsteroidField.spawn(new_radius, self.position, velocity1 * 1.2)
