import pygame
import pygame.sprite
import random

import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(players)
        self.image = load_image('Yellow dog\\1.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y


class Circle:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color('white'), (self.x, self.y), 10)


class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y, height, img, all_sprites=None):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.img_name = img
        self.image = load_image(self.img_name)
        self.height = height
        self.width = self.image.get_rect().size[0] / (self.image.get_rect().size[1] / self.height)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect().move(x, y)

    def move(self, x, y):
        self.x, self.y = x, y


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


class Wolf(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.indx=0
        self.indy=0
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
            if self.p_x > self.rect.x + 3:
                v_x = 2
            elif self.p_x - 3 < self.rect.x:
                v_x = -2
            if self.p_y - 3 > self.rect.y:
                v_y = 2
            elif self.p_y + 3 < self.rect.y:
                v_y = -2
        else:
            print(self.p_x, self.rect.x)
            if self.p_x - 3> self.rect.x:
                v_x = 4
            elif self.p_x + 3 < self.rect.x:
                v_x = -4
            if self.p_y - 3 > self.rect.y:
                v_y = 4
            elif self.p_y + 3 < self.rect.y:
                v_y = -4
        self.rect.y += v_y
        self.rect.x += v_x
        # self.ind+=0.025
        if v_x<0:
            self.image=load_image(f"wolf\\w{int(self.indx)%5+5}.png")

            self.indx+=0.025 * 4
        elif v_x>0:
            self.image=load_image(f"wolf\\w{int(self.indx)%5+5}.png")
            self.image = pygame.transform.flip(self.image, True, False)
            self.indx+=0.025 * 4
            # pygame.image.flip(screen, True, False)
        elif v_y<0:

            self.image=load_image(f"wolf\\w{int(self.indy)%4+10}.png")
            self.indy+=0.025 * 4
        else:
            # print(int(self.indy) % 4 + 10)
            self.image=load_image(f"wolf\\w{int(self.indy)%5}.png")
            self.indy += 0.025 * 4
        for i in wolfs:
            if pygame.sprite.collide_mask(self, i) and self != i:
                self.rect = self.rect.move(random.randint(-10, 10), random.randint(-10, 10))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('game')
    info = pygame.display.Info()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    circ = Circle(width // 2 + 250, height // 2, screen)
    circ_2 = Circle(width, height // 2, screen)
    circ_3 = Circle(width, height, screen)
    circ_4 = Circle(-10, -100, screen)
    objs = [circ, circ_2, circ_3, circ_4]

    players = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()

    fon = Fon(-5000, -4400, 'fon.png')

    '''for i in range(100):
        for j in range(50):
            Grass(j * 50, i * 100 - 2500, 100, '0c4a35590e197fd.png', all_sprites=all_sprites)'''

    player = Player(width // 2, height // 2)

    fps = 60
    clock = pygame.time.Clock()

    running = True

    u, d, r, l = False, False, False, False
    x = 0
    y = 0
    wolfs = pygame.sprite.Group()
    wolf = Wolf(-100, -100)
    wolf_2 = Wolf(500, -100)
    wolf_3 = Wolf(-100, 500)
    wolfs.add(wolf)
    wolfs.add(wolf_2)
    wolfs.add(wolf_3)
    while running:
        wolfs.update(player, wolfs)
        screen.fill(pygame.Color('black'))
        screen.blit(fon.image, (fon.x, fon.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    u = True
                elif event.key == pygame.K_DOWN:
                    d = True
                elif event.key == pygame.K_RIGHT:
                    r = True
                elif event.key == pygame.K_LEFT:
                    l = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    u = False
                elif event.key == pygame.K_DOWN:
                    d = False
                elif event.key == pygame.K_RIGHT:
                    r = False
                elif event.key == pygame.K_LEFT:
                    l = False
        if u:
            y += 5
        if d:
            y -= 5
        if r:
            x -= 5
        if l:
            x += 5
        for obj in objs:
            obj.x += x
            obj.y += y
            obj.draw()

        for spr in all_sprites:
            spr.move(x, y)
        fon.x += x
        fon.y += y
        wolf.rect.x += x
        wolf.rect.y += y
        wolf_2.rect.x += x
        wolf_2.rect.y += y
        wolf_3.rect.x += x
        wolf_3.rect.y += y
        screen.blit(wolf.image, (wolf.rect.x, wolf.rect.y))
        screen.blit(wolf_2.image, (wolf_2.rect.x, wolf_2.rect.y))
        screen.blit(wolf_3.image, (wolf_3.rect.x, wolf_3.rect.y))

        x = 0
        y = 0
        all_sprites.draw(screen)

        players.draw(screen)

        clock.tick(fps)

        pygame.display.flip()

    pygame.quit()