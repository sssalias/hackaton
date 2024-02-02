import pygame

from Functions import collision_cursor, collision_cursor_polz
from Texts import Text


class Settings:
    def __init__(self, screen, width, height):
        self.state = False
        self.screen = screen
        self.width = width
        self.height = height
        self.moving_1 = False
        self.moving_2 = False
        self.polz = Polz(width, height, 100, 100, 15, screen)
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

    def loop(self, event):
        self.buttonUpdate(self.screen, pygame.Color('grey'), event)
        self.musTxt.draw_text()
        self.volTxt.draw_text()
        self.exit.draw_text()
        self.polz.draw()

    def buttonUpdate(self, screen, color, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if collision_cursor(self.exit.x, self.exit.y, self.exit.width, self.exit.height, event.pos[0],
                                event.pos[1]):
                for scr in self.screens:
                    scr.state = False
                self.screens[0].state = True

            elif collision_cursor_polz(self.polz.x, self.polz.y, self.polz.size, event.pos[0], event.pos[1]):
                self.moving_1 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.moving_1 = False
        if event.type == pygame.MOUSEMOTION:
            if self.moving_1:
                self.polz.move(event.rel, event.pos)
        screen.fill(pygame.Color(color))


class Polz:
    def __init__(self, width, height, x, y, size, screen):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.vol = 0

    def draw(self):
        pygame.draw.line(self.screen, pygame.Color('black'), (100, 100), (100 + 100, 100), 5)
        pygame.draw.circle(self.screen, pygame.Color('blue'), (self.x, self.y), self.size)
        self.text = Text(40, str(self.vol), pygame.Color('Blue'), 230, 90, self.width, self.height, self.screen)
        self.text.draw_text()

    def move(self, rel, pos):
        if 100 < rel[0] + self.x < 200 and 100 < pos[0] < 200:
            self.x += rel[0]
            self.vol = self.x - 100
        elif pos[0] < 100:
            self.x = 100
            self.vol = 0
        elif pos[0] > 200:
            self.x = 200
            self.vol = 100
