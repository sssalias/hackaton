import pygame
from Functions import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img,  players=None, all_sprites=None):
        super().__init__(players, all_sprites)
        self.image = load_image(img)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y
