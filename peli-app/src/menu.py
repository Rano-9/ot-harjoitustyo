import pygame
from sprites.assets.button import Element_button

class Menu():
    def __init__(self,center,texts,font_size,txt_rgb,bg_rgb):
        self.text_surfaces = pygame.sprite.Group()
        for i,v in enumerate(texts):
            x,y = center
            self.text_surfaces.add(Element_button((x,y+i*50),v,font_size,txt_rgb,bg_rgb))
        
        pass