from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        # basic
        super().__init__(groups)
        self.image = pygame.image.load("space game/images/player.png")
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.acceleration = 1.002
        self.base_speed = 0.1
        self.speed = self.base_speed
        self.max_speed = 20
        self.direction = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = keys[int(pygame.K_RIGHT)] - keys[int(pygame.K_LEFT)]
        self.direction.y = keys[int(pygame.K_DOWN)] - keys[int(pygame.K_UP)]
        if not self.direction:
            self.speed = self.base_speed
        self.direction = self.direction.normalize() if self.direction else self.direction

    def movement(self,dt):
        if self.speed <= self.max_speed:
            self.speed *= self.acceleration
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def update(self,dt):
        self.input()
        self.movement(dt)

