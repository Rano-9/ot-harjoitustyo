import pygame
from sprites.elements import Element_score
from sprites.elements import Element_txt

class Score():
    def __init__(self,center,texts,font_size,txt_rgb,bg_rgb):
        self.surfaces = pygame.sprite.Group()
        x,y = center
        lose_txt = Element_txt((x,y-40),texts[0],font_size,txt_rgb,bg_rgb)
        piste_txt = Element_txt((x,y-0),"Pisteesi",font_size,txt_rgb,bg_rgb)
        score = Element_score((x,y+40),0,font_size,txt_rgb,bg_rgb)
#       restart_button = Element_button((x,y+50),"RESTART",font_size,txt_rgb,bg_rgb)

#       self.surfaces.add(restart_button)
        self.surfaces.add(lose_txt)
        self.surfaces.add(piste_txt)
        self.surfaces.add(score)
