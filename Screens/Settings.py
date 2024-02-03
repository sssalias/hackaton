import pygame

from Functions import collision_cursor, collision_cursor_polz
from Utilities.Texts import Text


class Settings:
    def __init__(self, screen, width, height):
        self.state = False
        self.screen = screen
        self.width = width
        self.height = height
        self.moving_1 = False
        self.moving_2 = False
        self.polz = Polz(width, height, 500, self.width / 3 + 15, 15, 500, 600, screen)
        self.polz_2 = Polz(width, height, 500, self.width / 2.2 + 15, 15, 500, 600, screen)
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
        self.polz_2.draw()

    def buttonUpdate(self, screen, color, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if collision_cursor(self.exit.x, self.exit.y, self.exit.width, self.exit.height, event.pos[0],
                                event.pos[1]):
                for scr in self.screens:
                    scr.state = False
                self.screens[0].state = True

            elif collision_cursor_polz(self.polz.x, self.polz.y, self.polz.size, event.pos[0], event.pos[1]):
                self.moving_1 = True
            elif collision_cursor_polz(self.polz_2.x, self.polz_2.y, self.polz_2.size, event.pos[0], event.pos[1]):
                self.moving_2 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.moving_1 = False
            self.moving_2 = False
        if event.type == pygame.MOUSEMOTION:
            if self.moving_1:
                self.polz.move(event.rel, event.pos)
            if self.moving_2:
                self.polz_2.move(event.rel, event.pos)
        screen.fill(pygame.Color(color))


class Polz:
    def __init__(self, width, height, x, y, size, left, right, screen):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.vol = 0
        self.left = left
        self.right = right

    def draw(self):
        pygame.draw.line(self.screen, pygame.Color('black'), (self.left, self.y), (self.right, self.y), 5)
        pygame.draw.circle(self.screen, pygame.Color('blue'), (self.x, self.y), self.size)
        self.text = Text(40, str(self.vol), pygame.Color('Blue'), self.right + 30, self.y - 10, self.width, self.height, self.screen)
        self.text.draw_text()

    def move(self, rel, pos):
        if self.left < rel[0] + self.x < self.right and self.left < pos[0] < self.right:
            self.x += rel[0]
            self.vol = self.x - self.left
        elif pos[0] < self.left:
            self.x = self.left
            self.vol = 0
        elif pos[0] > self.right:
            self.x = self.right
            self.vol = 100
