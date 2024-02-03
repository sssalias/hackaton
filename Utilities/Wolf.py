import random

import pygame
from Utilities.Functions import load_image


class Wolf(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.p_x = width // 2
        self.p_y = height // 2
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, other, wolfs):

        razn_x = (self.p_x - self.rect.x) ** 2
        razn_y = (self.p_y - self.rect.y) ** 2
        v_x = 0
        v_y = 0
        if (razn_y + razn_x) ** 0.5 > 1000:
            if self.p_x > self.rect.x:
                v_x = 2
            elif self.p_x < self.rect.x:
                v_x = -2
            if self.p_y > self.rect.y:
                v_y = 2
            elif self.p_y < self.rect.y:
                v_y = -2
        else:
            print(self.p_x > self.rect.x, self.p_x, self.rect.x)
            if self.p_x > self.rect.x:
                v_x = 4
            elif self.p_x < self.rect.x:
                v_x = -4
            if self.p_y > self.rect.y:
                v_y = 4
            elif self.p_y < self.rect.y:
                v_y = -4
        self.rect.y += v_y
        self.rect.x += v_x
        self.image = load_image('Yellow dog\\2.png')
        for i in wolfs:
            if pygame.sprite.collide_mask(self, i) and self != i:
                self.rect = self.rect.move(random.randint(-10, 10), random.randint(-10, 10))
