import pygame
from Texts import Text
from Functions import collision_cursor


class Settings:
    def __init__(self, screen, width, height):
        self.state = False
        self.screen = screen
        self.width = width
        self.height = height
        self.exit = Text(60, 'X', pygame.Color('Blue'), 0, 0, self.width,
                         self.height, self.screen, button=True)
        self.volTxt = Text(60, 'Volume', pygame.Color('Blue'), self.height // 2 - 200, self.width / 3, self.width,
                           self.height, self.screen)
        self.musTxt = Text(60, 'Music', pygame.Color('Blue'), self.height // 2 - 200, self.width / 2.2, self.width,
                           self.height, self.screen)

    def add(self, screens):
        self.screens = screens

    def update(self):
        pass

    def loop(self):
        self.musTxt.draw_text()
        self.volTxt.draw_text()
        self.exit.draw_text()

    def buttonUpdate(self, event, screen, color):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if collision_cursor(self.exit, event):
                for scr in self.screens:
                    scr.state = False
                screen.fill(pygame.Color(color))
                self.screens[0].state = True
