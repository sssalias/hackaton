import pygame
from Texts import Text
from Functions import collision_cursor


class Menu:
    def __init__(self, screen, width, height):
        self.state = True
        self.screen = screen
        self.width = width
        self.height = height
        self.text = Text(60, 'НАЗВАНИЕ', pygame.Color('Blue'), self.height // 2, self.width / 3, self.width,
                         self.height, self.screen)
        self.btn = Text(60, 'SETTINGS', pygame.Color('Blue'), self.height // 2, self.width / 2.2, self.width,
                        self.height, self.screen, button=True)

    def add(self, screens):
        self.screens = screens

    def update(self):
        pass

    def loop(self):
        self.text.draw_text()
        self.btn.draw_text()

    def buttonUpdate(self, event, screen, color):
       if event.type == pygame.MOUSEBUTTONDOWN:
            if collision_cursor(self.btn.x, self.btn.y, self.btn.width, self.btn.height, event.pos[0], event.pos[1]):
                for scr in self.screens:
                    scr.state = False
                screen.fill(pygame.Color(color))
                self.screens[1].state = True

