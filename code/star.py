from settings import *

class Star(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("space game/images/star.png")
        self.rect = self.image.get_frect(center = pos)