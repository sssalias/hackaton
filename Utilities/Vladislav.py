import pygame
from Utilities.Texts import Text

class Host:
    def __init__(self, pos_x, pos_y, image, screen, width, height):
        self.image = image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y
        self.height = 150
        self.screen = screen
        self.width = self.image.get_rect().size[0] / (self.image.get_rect().size[1] / self.height)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.text = Text(40, 'press E', pygame.Color('white'), 500, 400, width, height, self.screen)

    def say(self):
        self.text.draw_text()

    def draw(self):

    def win(self):
        pass