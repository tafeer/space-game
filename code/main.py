from settings import *
from player import Player
from star import Star
from random import randint

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Space Game")
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        
        # stars
        for i in range(20):
            Star((randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)), (self.all_sprites))

        # player
        self.player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), (self.all_sprites))

        # asteroids

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # updating the screen
            self.display_surface.fill("Black")
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()