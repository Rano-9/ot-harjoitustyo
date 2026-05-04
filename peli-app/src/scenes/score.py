import pygame
from sprites.elements import Element_score
from sprites.elements import Element_txt

class Score():
    """
    Luokka joka käsittelee Menu näkymän elementtejä

    Attributes:
        type: Näkymän tyyppi (score_scene).
        surfaces: Sprite group joka sisältää luokan elementit

    """

    def __init__(self,center:tuple,text:bool,font_size:int,txt_rgb:tuple,bg_rgb:tuple):
        """
        Luokan konstruktori, luo uuden näkymän

        Args:
            center: Näkymän keskipiste (x,y)
            text: Lisätäänkö häviämisteksti (bool)
            font_size: Fonttikoko tekstille (int)
            txt_rgb: teksin väri (r,g,b)
            bg_rgb: tesktin taustaväri (r,g,b)
        """


        self.surfaces = pygame.sprite.Group()
        x,y = center

        if text:
            lose_txt = Element_txt((x,y-40),"Ei mahdollisia liikkeitä",font_size,txt_rgb,bg_rgb)
        piste_txt = Element_txt((x,y-0),"Pisteesi",font_size,txt_rgb,bg_rgb)
        score = Element_score((x,y+40),0,font_size,txt_rgb,bg_rgb)

        if text:
            self.surfaces.add(lose_txt)
        self.surfaces.add(piste_txt)
        self.surfaces.add(score)

    @property
    def type(self):
        """
        Luokan tyyppi getter

        Returns:
            "score_scene"
        """
        return "score_scene"
