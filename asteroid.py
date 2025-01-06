import pygame
from constants import *
from player import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(- random_angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2
