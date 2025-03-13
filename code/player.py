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
        x = keys[int(pygame.K_RIGHT)] - keys[int(pygame.K_LEFT)]
        y = keys[int(pygame.K_DOWN)] - keys[int(pygame.K_UP)]
        self.is_moving = x or y
        if self.is_moving:
            self.direction = pygame.math.Vector2(x, y).normalize()

    def movement(self,dt):
        if self.speed <= self.max_speed and self.is_moving:
            self.speed += self.acceleration * dt
        elif self.speed >= 0 and not self.is_moving:
            self.speed -= self.deceleration * dt
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def update(self,dt):
        self.input()
        self.movement(dt)

