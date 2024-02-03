import pygame
import pygame.sprite

import os
import sys

import random


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
        self.image = load_image('people\\part1_1.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y
        self.height = 150
        self.width = self.image.get_rect().size[0] / (self.image.get_rect().size[1] / self.height)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


class Circle:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color('white'), (self.x, self.y), 10)


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
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
        #if not f:
            #self.kill()



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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('game')
    info = pygame.display.Info()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    trees = pygame.sprite.Group()

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

    imgs = [load_image('kyst.png'), load_image('pen.png'), load_image('treeBig.png'), load_image('treeMed.png'), load_image('treeSm.png'), load_image('treeVSm.png')]
    for i in range(1000):
        x2 = random.randint(-10000, 0)
        y2 = random.randint(-5000, 0)
        trees.add(Tree(x2, y2, random.choice(imgs)))

    f = (x2 > (player.x - width // 2) and x2 < (player.x + width // 2)) and (y2 < (player.y + height // 2) and y2 > (player.y - height // 2))

    while running:






        for el in trees:
            el.move(x, y)

        screen.fill(pygame.Color('black'))
        screen.blit(fon.image, (fon.x, fon.y))
        #print(fon.x, fon.image.get_rect().size[0], fon.y, fon.image.get_rect().size[1])
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

        x = 0
        y = 0
        all_sprites.draw(screen)

        players.draw(screen)

        trees.draw(screen)

        clock.tick(fps)

        for el in trees:
            print(el)

        pygame.display.flip()

    pygame.quit()
