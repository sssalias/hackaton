import pygame
from Screens.Screen import Screen
from Screens.Menu import Menu
from Screens.Settings import Settings
from Screens.Level import Level


class Game(Screen):
    def __init__(self):
        self.running = True
        self.color = 'gray'
        super().__init__(self.color)
        self.menu = Menu(self.screen, self.width, self.height)
        self.settings = Settings(self.screen, self.width, self.height)
        self.level = Level(self.screen, self.width, self.height)
        self.screens = [self.menu, self.settings, self.level]
        for scr in self.screens:
            scr.add(self.screens)

    def run(self):
        self.main_loop(self.screen)

    def main_loop(self, screen):
        ev = ''
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                ev = event
            for scr in self.screens:
                if scr.state:
                    if ev != '':
                        scr.loop(event=ev)
                    else:
                        scr.loop()
            self.clock.tick(self.fps)
            pygame.display.flip()
        pygame.quit()
