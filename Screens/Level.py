import pygame
from Utilities.Texts import Text
from Utilities.Player import Player
from Utilities.Fon import Fon
from Utilities.Wolf import Wolf


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
        self.wolfs = pygame.sprite.Group()
        self.wolf = Wolf(-1000, -1000, width, height)
        self.wolf_2 = Wolf(5000, -1000, width, height)
        self.wolf_3 = Wolf(-1000, 2000, width, height)
        self.wolfs.add(self.wolf)
        self.wolfs.add(self.wolf_2)
        self.wolfs.add(self.wolf_3)
        self.u, self.d, self.r, self.l = False, False, False, False
        self.move_x = 0
        self.move_y = 0
        self.objs = []
        self.fon = Fon(-5000, -4200, 'fon.png')
        self.night = False

    def add(self, screens):
        self.screens = screens

    def loop(self, event=''):
        self.screen.fill(pygame.Color('Blue'))
        self.wolfs.update(self.player, self.wolfs)
        self.player.selectAnim(self.r, self.l, self.u, self.d)
        if self.moove():
            for obj in self.objs:
                obj.x += self.move_x
                obj.y += self.move_y
                obj.draw()
            self.fon.x += self.move_x
            self.fon.y += self.move_y
        self.screen.blit(self.fon.image, (self.fon.x, self.fon.y))
        if self.night:
            self.wolf.rect.x += self.move_x
            self.wolf.rect.y += self.move_y
            self.wolf_2.rect.x += self.move_x
            self.wolf_2.rect.y += self.move_y
            self.wolf_3.rect.x += self.move_x
            self.wolf_3.rect.y += self.move_y
            self.screen.blit(self.wolf.image, (self.wolf.rect.x, self.wolf.rect.y))
            self.screen.blit(self.wolf_2.image, (self.wolf_2.rect.x, self.wolf_2.rect.y))
            self.screen.blit(self.wolf_3.image, (self.wolf_3.rect.x, self.wolf_3.rect.y))
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
                self.u = True
                self.d = False
                self.move_y = 5
            elif event.key == pygame.K_DOWN:
                self.d = True
                self.u = False
                self.move_y = -5
            elif event.key == pygame.K_RIGHT:
                self.r = True
                self.l = False
                self.move_x = -5
            elif event.key == pygame.K_LEFT:
                self.l = True
                self.r = False
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

    def moove(self):
        print(self.fon.x + self.move_x, self.fon.y + self.move_y)
        if -9000 < self.fon.x + self.move_x < 0 and -4200 < self.fon.y + self.move_y < 0:
            return True
        return False

