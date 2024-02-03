from Utilities.Functions import load_image


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
