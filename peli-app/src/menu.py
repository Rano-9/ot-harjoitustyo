import pygame
from sprites.button import Element_button

class Menu():
    def __init__(self,center,texts,font_size,txt_rgb,bg_rgb):
        self.surfaces = pygame.sprite.Group()
        for i,v in enumerate(texts):
            x,y = center
            self.surfaces.add(Element_button((x,y+i*50),v,font_size,txt_rgb,bg_rgb))
