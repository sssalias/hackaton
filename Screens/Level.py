import pygame
from Texts import Text


class Level:
    def __init__(self, screen, width, height):
        self.screens = None
        self.state = False
        self.screen = screen
        self.width = width
        self.height = height
        self.leave = Text(40, "Press esc to leave", pygame.Color('white'), 400, 350, width, height, screen)
        self.draw = False

    def add(self, screens):
        self.screens = screens

    def loop(self, event):
        self.screen.fill(pygame.Color('Red'))
        self.events(event)
        if self.draw:
            self.leave.draw_text()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.type == 768 and not self.draw:
                self.draw = True
            elif event.type == 768 and self.draw:
                for scr in self.screens:
                    scr.state = False
                self.screens[0].state = True
                self.draw = False
            elif event.type != pygame.K_ESCAPE:
                self.draw = False

