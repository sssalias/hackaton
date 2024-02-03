import pygame
from Utilities.Texts import Text

WHITE = (255, 255, 255)
w = 150
h = 150
W = 1000
H = 800
X = 900
Y = 50


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (W / 2, H / 2)
        self.leave = Text(40, "press", pygame.Color("black"), 500, 400, W, H, screen)
        self.draw = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self, event):
        x = 0
        y = 0
        if event.type == pygame.KEYDOWN:
            print(event.key, pygame.K_a)
            if event.key == pygame.K_a:
                self.left = True
            elif event.key == pygame.K_d:
                self.right = True
            elif event.key == pygame.K_w:
                self.up = True
            elif event.key == pygame.K_s:
                self.down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.left = False
            elif event.key == pygame.K_d:
                self.right = False
            elif event.key == pygame.K_w:
                self.up = False
            elif event.key == pygame.K_s:
                self.down = False
        if self.left:
            x = -25
        elif self.right:
            x = 25
        elif self.up:
            y = -25
        elif self.down:
            y = 25
        self.rect.x += x
        self.rect.y += y
        self.image = pygame.image.load("data/Enemy_2_1.png")

    def loop(self, event):
        self.update(event)
        self.event(event)
        if self.draw:
            self.leave.draw_text()
            # font = pygame.font.Font(None, 36)
            # text = font.render("Hello, world!", True, (255, 255, 255))

    def event(self, event):
        if event.type == pygame.KEYDOWN and not self.draw:
            if event.key == pygame.K_e and (X - 320 <= self.rect.x <= X + 320 and Y - 320 <= self.rect.y <= Y + 320):
                self.draw = True
        elif event.type == pygame.KEYDOWN and self.draw:
            self.draw = False


pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("заголовок")
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
fps = 60
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        player.loop(event)
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, (0, 0, 0), (X, Y), 5)
    all_sprites.draw(screen)

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()