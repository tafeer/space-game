from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("space game/images/player.png")
        self.rect = self.image.get_frect(center = pos)

        # movement
        self.acceleration = 10
        self.deceleration = 20
        self.speed = 0
        self.max_speed = 40
        self.direction = pygame.math.Vector2()
        self.last_direction = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = keys[int(pygame.K_RIGHT)] - keys[int(pygame.K_LEFT)]
        self.direction.y = keys[int(pygame.K_DOWN)] - keys[int(pygame.K_UP)]
        self.direction = self.direction.normalize() if self.direction else self.direction

    def movement(self,dt):
        if self.speed <= self.max_speed and keys:
            self.speed += self.acceleration * dt
        elif self.speed >= 0 and not keys:
            self.speed -= self.deceleration * dt
        self.rect.x += self.last_direction.x * self.speed * dt
        self.rect.y += self.last_direction.y * self.speed * dt

    def update(self,dt):
        self.input()
        self.movement(dt)

