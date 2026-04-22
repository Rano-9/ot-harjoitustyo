import pygame
from sprites.elements import Element_button
from sprites.elements import Element_txt

class Score():
    def __init__(self,center,texts,font_size,txt_rgb,bg_rgb):
        self.surfaces = pygame.sprite.Group()
        x,y = center
        lose_text = Element_button((x,y-25),texts[0],font_size,txt_rgb,bg_rgb)
        score = Element_button((x,y+25),0,font_size,txt_rgb,bg_rgb)
#        restart_button = Element_button((x,y+50),"RESTART",font_size,txt_rgb,bg_rgb)

#        self.surfaces.add(restart_button)
        self.surfaces.add(lose_text)
        self.surfaces.add(score)
