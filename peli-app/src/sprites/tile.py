import os
from random import randint

import pygame

dirname = os.path.dirname(__file__)


class Tile(pygame.sprite.Sprite):

    def __init__(self, loc=None):
        super().__init__()

        self.location = loc
        self.hits = 0
        self.image = None
        self.num = None
        self.prev = self.num
        self.click()
        self.rect = self.image.get_rect()
        
    
    def click(self):
        if self.num:
            prev = self.num
        
        self.num = self.new_num()

        if not self.prev:
            self.prev = self.num
        
        color = ""
        path = None
        match self.hits:
            case 0:
                color = "green"
                path = os.path.join(dirname, "assets",
                                    color, f"{self.num}.png")
            case 1:
                color = "yellow"
                path = os.path.join(dirname, "assets",
                                    color, f"{self.num}.png")
            case 2:
                color = "red"
                path = os.path.join(dirname, "assets",
                                    color, f"{self.num}.png")
            case 3:
                self.image.fill((0, 0, 0))

        self.hits += 1

        if path is not None:
            self.image = pygame.image.load(path)

        return (self.prev, self.location)

    def new_num(self):
        num = randint(1, 4)

        return num
