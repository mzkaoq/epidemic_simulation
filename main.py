import pygame
from game_package.game import Game
from game_package.constant import FPS_RATE, SCALE, AREA

FPS = FPS_RATE
WIN = pygame.display.set_mode((SCALE * AREA, SCALE * AREA))
pygame.display.set_caption("COVID-19 visualization")
game = Game(WIN)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game._init()
        game.update()
        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()