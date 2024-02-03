import random

import pygame
from Utilities.Functions import load_image


class Wolf(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.indx = 0
        self.indy = 0
        self.p_x = width // 2
        self.p_y = height // 2
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, other, wolfs):
        self.p_x = other.x
        self.p_y = other.y
        razn_x = (self.p_x - self.rect.x) ** 2
        razn_y = (self.p_y - self.rect.y) ** 2
        v_x = 0
        v_y = 0
        if (razn_y + razn_x) ** 0.5 > 1000:
            if self.p_x > self.rect.x:
                v_x = 1
            elif self.p_x < self.rect.x:
                v_x = -1
            if self.p_y > self.rect.y:
                v_y = 1
            elif self.p_y < self.rect.y:
                v_y = -1
        else:
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
        if v_x < 0:
            self.image = load_image(f"wolf\\w{int(self.indx) % 5 + 5}.png")

            self.indx += 0.025 * 4
        elif v_x > 0:
            self.image = load_image(f"wolf\\w{int(self.indx) % 5 + 5}.png")
            self.image = pygame.transform.flip(self.image, True, False)
            self.indx += 0.025 * 4
            # pygame.image.flip(screen, True, False)
        elif v_y < 0:

            self.image = load_image(f"wolf\\w{int(self.indy) % 4 + 10}.png")
            self.indy += 0.025 * 4
        else:
            # print(int(self.indy) % 4 + 10)
            self.image = load_image(f"wolf\\w{int(self.indy) % 5}.png")
            self.indy += 0.025 * 4
        for i in wolfs:
            if pygame.sprite.collide_mask(self, i) and self != i:
                self.rect = self.rect.move(random.randint(-10, 10), random.randint(-10, 10))
