import pygame
from sprites.elements import Element_button

class Menu():
    def __init__(self,center,texts,font_size,txt_rgb,bg_rgb):
        self.surfaces = pygame.sprite.Group()
        x,y = center
        start_button = Element_button((x,y),texts[0],font_size,txt_rgb,bg_rgb,"game")
        quit_button = Element_button((x,y+50),texts[1],font_size,txt_rgb,bg_rgb,"quit")

        self.surfaces.add(start_button)
        self.surfaces.add(quit_button)
