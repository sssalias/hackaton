import pygame


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, trees, all_sprites):
        super().__init__(trees, all_sprites)
        self.image = image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y
        self.height = 150
        self.width = self.image.get_rect().size[0] / (self.image.get_rect().size[1] / self.height)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.d = image


    def update(self, v=None):
        if v == 'night':
            self.image = 0
        else:
            self.image = self.d

    def move(self, x, y):
        self.x += x
        self.y += y
        self.rect = self.image.get_rect().move(self.x, self.y)