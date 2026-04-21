import os
from random import randint

import pygame

dirname = os.path.dirname(__file__)


class Tile(pygame.sprite.Sprite):

    def __init__(self, index, loc=None):
        super().__init__()
        self._id = None
        self.allow = True
        self.location = loc
        self.hits = 0
        self.num = self.new_num()
        border_path = os.path.join(dirname,"assets","highlight.png")
        path = os.path.join(dirname, "assets", "green",f"{self.num}.png")        
        self.images = [pygame.image.load(path),pygame.image.load(border_path)]
        self.rects = [self.images[0].get_rect(center=loc),self.images[1].get_rect(center=loc)]
        
    @property
    def rect(self):
        return self.rects[0]
    
    @property
    def image(self):
        return self.images[0]
    
    @image.setter
    def image(self, path):
        self.images[0] = pygame.image.load(path)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        self._id = value
        print("set value",self._id)


    def draw(self,surface):
        surface.blit(self.image,self.rect)

        if self.allow:
            surface.blit(self.images[1],self.rect)


    def update(self, allowed,surface):
        if self.id in allowed:
            self.allow = True
        else:
            self.allow = False
        
        self.draw(surface)
        
        

    def click(self):
        prev = self.num
        
        self.num = self.new_num()
        path = None
        self.hits += 1
        
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

        if path is not None:
            self.image = path

        return (prev, self.id)

    def new_num(self):
        num = randint(1, 4)

        return num
