import pygame
from Screen import Screen
from menu import Menu
from settings import Settings


class Game(Screen):
    def __init__(self):
        self.running = True
        self.color = 'gray'
        super().__init__(self.color)
        self.menu = Menu(self.screen, self.width, self.height)
        self.settings = Settings(self.screen, self.width, self.height)
        self.screens = [self.menu, self.settings]
        for scr in self.screens:
            scr.add(self.screens)

    def run(self):
        self.main_loop(self.screen)

    def main_loop(self, screen):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for scr in self.screens:
                    if scr.state:
                        scr.loop(event)
            pygame.display.flip()
        pygame.quit()
