from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        # basic
        super().__init__(groups)
        self.image = pygame.image.load("space game/images/player.png")
        self.rect = self.image.get_frect(center = pos)

    def update(self):
        pass