import pygame
from Utilities.Functions import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img,  players=None):
        super().__init__(players)
        self.image = load_image('people\\part1_1.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y
        self.height = 150
        self.width = self.image.get_rect().size[0] / (self.image.get_rect().size[1] / self.height)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.animR = [load_image('people\\part1_10.png'), load_image('people\\part1_11.png'),
                      load_image('people\\part1_12.png'), load_image('people\\part1_11.png'),
                      load_image('people\\part1_10.png')]

        self.animL = [load_image('people\\part1_4.png'), load_image('people\\part1_5.png'),
                      load_image('people\\part1_6.png'), load_image('people\\part1_5.png'),
                      load_image('people\\part1_4.png')]

        self.animD = [load_image('people\\part1_1.png'), load_image('people\\part1_2.png'),
                      load_image('people\\part1_3.png'), load_image('people\\part1_2.png'),
                      load_image('people\\part1_1.png')]

        self.animU = [load_image('people\\part1_7.png'), load_image('people\\part1_8.png'),
                      load_image('people\\part1_9.png'), load_image('people\\part1_8.png'),
                      load_image('people\\part1_7.png')]

        self.p = self.image
        self.number = 1 / 10

    def selectAnim(self, r, l, u, d):
        if r:
            self.animation(self.animR)
        elif l:
            self.animation(self.animL)
        elif d:
            self.animation(self.animD)
        elif u:
            self.animation(self.animU)
        else:
            self.image = self.p
        self.number += 1 / 10
        self.rect = self.image.get_rect().move(self.x, self.y)

    def animation(self, anim):
        self.image = anim[round(self.number) % len(anim)]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
