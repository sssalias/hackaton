import pygame


class Screen:
    FPS = 60
    COLORS = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "gray": (128, 128, 128),
        "red": (255, 0, 0)
    }

    def __init__(self, color) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        nf = pygame.NOFRAME
        self.running = True
        pygame.display.set_caption('game')
        info = pygame.display.Info()
        size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(self.COLORS[color])
