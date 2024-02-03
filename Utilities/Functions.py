import os
import sys
import pygame

def collision_cursor(a_x, a_y, a_width, a_height, b_x, b_y):
    if a_x - 10 < b_x < a_x + a_width + 10 and a_y - 10 < b_y < a_y + a_height + 10:
        return True
    else:
        return False


def collision_cursor_polz(a_x, a_y, a_size, b_x, b_y):
    if a_x - a_size < b_x < a_x + a_size and a_y - a_size < b_y < a_y + a_size:
        return True
    else:
        return False

def load_image(name, colorkey=None):
    fullname = os.path.join('../data', name)
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