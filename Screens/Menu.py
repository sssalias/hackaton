import pygame
from Texts import Text
from Functions import collision_cursor


class Menu:
    def __init__(self, screen, width, height):
        self.state = True
        self.screen = screen
        self.width = width
        self.height = height
        self.text = Text(60, 'НАЗВАНИЕ', pygame.Color('Blue'), self.height // 2, self.width / 3 - 150, self.width,
                         self.height, self.screen)
        self.btn_1 = Text(60, 'SETTINGS', pygame.Color('Blue'), self.height // 2 + 150, self.width / 2.2, self.width,
                        self.height, self.screen, button=True)
        self.btn_2 = Text(60, 'New Game', pygame.Color('Blue'), self.height // 2 - 150, self.width / 2.2, self.width,
                        self.height, self.screen, button=True)

    def add(self, screens):
        self.screens = screens

    def update(self):
        pass

    def loop(self, event):
        self.buttonUpdate(self.screen, pygame.Color('grey'), event)
        self.text.draw_text()
        self.btn_1.draw_text()
        self.btn_2.draw_text()

    def buttonUpdate(self, screen, color, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if collision_cursor(self.btn_1.x, self.btn_1.y, self.btn_1.width, self.btn_1.height, event.pos[0], event.pos[1]):
                for scr in self.screens:
                    scr.state = False
                self.screens[1].state = True
            elif collision_cursor(self.btn_2.x, self.btn_2.y, self.btn_2.width, self.btn_2.height, event.pos[0], event.pos[1]):
                for scr in self.screens:
                    scr.state = False
                self.screens[2].state = True
        screen.fill(pygame.Color(color))

