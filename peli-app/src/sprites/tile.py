import pygame
import os
dirname = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):

    def __init__(self, x =0, y= 0, id=None):
        super().__init__()
        self.id = id
        self.image = pygame.image.load(
            os.path.join(dirname,"..","assets","tile.png")
        )
        self.location = (x,y)
        self.rect = self.image.get_rect()

    def click(self):
        self.image = pygame.image.load(
            os.path.join(dirname,"..","assets","tile1.png")
        )