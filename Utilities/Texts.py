import pygame


class Text:
    def __init__(self, size, txt, color, x, y, width, height, screen, button=False, round=False, font=None):
        self.color = color
        self.font_update = font
        self.size = size
        self.font = pygame.font.Font(font, self.size)
        self.text = self.font.render(txt, False, color)
        self.width = self.text.get_width()
        self.height = self.text.get_height()
        self.x = x
        self.y = y
        self.button = button
        self.round = round
        self.ready = False
        self.screen_width = width
        self.screen_height = height
        self.screen = screen

    def draw_text(self):
        if self.ready:
            pygame.draw.rect(self.screen, (134, 181, 13), (self.x - 10, self.y - 10,
                                                      self.width + 20, self.height + 20), 0)
        self.screen.blit(self.text, (self.x, self.y))
        if self.button:
            pygame.draw.rect(self.screen, (250, 255, 0), (self.x - 10, self.y - 10,
                                                     self.width + 20, self.height + 20), 1)
