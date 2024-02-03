import pygame
from Utilities.Texts import Text
from Utilities.Player import Player
from Utilities.Fon import Fon


class Level:
    def __init__(self, screen, width, height):
        self.screens = None
        self.state = False
        self.screen = screen
        self.width = width
        self.height = height
        self.leave = Text(40, "Press esc to leave", pygame.Color('white'), 400, 350, width, height, screen)
        self.draw = False
        self.players = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        self.player = Player(width / 2, height / 2, 'new_yellow_dog\yellow_dog_11.png', players=self.players)
        self.u, self.d, self.r, self.l = False, False, False, False
        self.move_x = 0
        self.move_y = 0
        self.objs = []
        self.fon = Fon(-5000, -4200, 'fon.png')

    def add(self, screens):
        self.screens = screens

    def loop(self, event=''):
        self.screen.fill(pygame.Color('Blue'))
        print(self.move_y, self.move_x)
        for obj in self.objs:
            obj.x += self.move_x
            obj.y += self.move_y
            obj.draw()
        self.fon.x += self.move_x
        self.fon.y += self.move_y
        self.screen.blit(self.fon.image, (self.fon.x, self.fon.y))
        if event != '':
            self.events(event)
        self.players.draw(self.screen)
        if self.draw:
            self.leave.draw_text()

    def events(self, event=''):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not self.draw:
                self.draw = True
            elif event.key == pygame.K_ESCAPE and self.draw:
                for scr in self.screens:
                    scr.state = False
                self.screens[0].state = True
                self.draw = False
            elif event.key == pygame.K_RETURN:
                self.draw = False
            if event.key == pygame.K_UP:
                print('hi')
                self.u = True
                self.move_y = 5
            elif event.key == pygame.K_DOWN:
                self.d = True
                self.move_y = -5
            elif event.key == pygame.K_RIGHT:
                self.r = True
                self.move_x = -5
            elif event.key == pygame.K_LEFT:
                self.l = True
                self.move_x = 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.u = False
                self.move_y = 0
            elif event.key == pygame.K_DOWN:
                self.d = False
                self.move_y = 0
            elif event.key == pygame.K_RIGHT:
                self.r = False
                self.move_x = 0
            elif event.key == pygame.K_LEFT:
                self.l = False
                self.move_x = 0


