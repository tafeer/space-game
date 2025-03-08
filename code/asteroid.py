from settings import *
from random import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.load("space game/images/asteroid.png")
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.speed = randint(30,50)
        self.direction = pygame.math.Vector2()

    def movement(self, dt):
        if pos[0] < 0:
            self.direction.x = random()
        else:
            self.direction.x = random() - 1
        if pos[1] < 0:
            self.direction.y = random()
        else:
            self.direction.y = random() - 1
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def update(self, dt):
        movement(dt)