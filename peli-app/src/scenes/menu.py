import pygame
from sprites.elements import Element_button

class Menu():
    """
    Luokka joka käsittelee Menu näkymän elementtejä

    Attributes:
        type: Näkymän tyyppi (menu_scene).
        surfaces: Sprite group joka sisältää luokan elementit

    """


    def __init__(self,center:tuple,texts:list,font_size:int,txt_rgb:tuple,bg_rgb:tuple):
        """
        Luokan konstruktori, luo uuden näkymän

        Args:
            center: Näkymän keskipiste (x,y)
            texts: Lista teksteistä jotka syötetään elementeille
            font_size: Fonttikoko tekstille
            txt_rgb: teksin väri (r,g,b)
            bg_rgb: tesktin taustaväri (r,g,b)
        """


        self.surfaces = pygame.sprite.Group()
        x,y = center
        start_button = Element_button((x,y),texts[0],font_size,txt_rgb,bg_rgb,"game")
        quit_button = Element_button((x,y+50),texts[1],font_size,txt_rgb,bg_rgb,"quit")

        self.surfaces.add(start_button)
        self.surfaces.add(quit_button)

    @property
    def type(self):
        """
        Luokan tyyppi getter

        Returns:
            "menu_scene"
        """
        return "menu_scene"
