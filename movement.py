import pygame
import pygame.sprite

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
        super().__init__(players, all_sprites)
        self.image = load_image('0c4a35590e197fd.png')
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

    player = Player(width // 2, height // 2)

    fps = 60
    clock = pygame.time.Clock()

    running = True

    u, d, r, l = False, False, False, False
    x = 0
    y = 0

    while running:
        screen.fill(pygame.Color('black'))
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

        x = 0
        y = 0

        players.draw(screen)

        clock.tick(fps)

        pygame.display.flip()

    pygame.quit()