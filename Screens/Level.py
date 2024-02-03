import pygame
from Utilities.Texts import Text
from Utilities.Player import Player
from Utilities.Functions import load_image


class Level:
    def __init__(self, screen, width, height):
        self.screens = None
        self.state = False
        self.screen = screen
        self.width = width
        self.height = height
        self.leave = Text(40, "Press esc to leave", pygame.Color('white'), 400, 350, width, height, screen)
        self.draw = False
        players = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        self.player = Player(0, 0, 'new_yellow_dog\yellow_dog_11.png', players=players, all_sprites=all_sprites)
        self.u, self.d, self.r, self.l = False, False, False, False
        self.move_x = 0
        self.move_y = 0
        self.objs = []
        self.fon = Fon(-5000, -4400, 'fon.png')

    def add(self, screens):
        self.screens = screens

    def loop(self, event):
        if self.u:
            self.move_y += 5
        if self.d:
            self.move_y -= 5
        if self.r:
            self.move_x -= 5
        if self.l:
            self.move_x += 5
        for obj in self.objs:
            obj.x += self.move_x
            obj.y += self.move_y
            obj.draw()
        self.screen.blit(self.fon.image, (self.fon.x, self.fon.y))
        self.events(event)
        if self.draw:
            self.leave.draw_text()

    def events(self, event):
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
            elif event.key == pygame.K_DOWN:
                self.d = True
            elif event.key == pygame.K_RIGHT:
                self.r = True
            elif event.key == pygame.K_LEFT:
                self.l = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.u = False
            elif event.key == pygame.K_DOWN:
                self.d = False
            elif event.key == pygame.K_RIGHT:
                self.r = False
            elif event.key == pygame.K_LEFT:
                self.l = False


class Fon:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img_name = img
        self.image = load_image(self.img_name)
        self.rect = self.image.get_rect().move(x, y)

    def move(self, x, y):
        self.x += x
        self.y += y
        self.rect = self.image.get_rect().move(self.x, self.y)

