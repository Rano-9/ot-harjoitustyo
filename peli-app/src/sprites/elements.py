import pygame
import pygame.freetype
from pygame.sprite import Sprite

#Teksti alustojen luonti

def create_text_element(text, font_size, txt_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=txt_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class Element_button(Sprite):
    def __init__(self,center,text,font_size,txt_rgb,bg_rgb,action=None):
        super().__init__()

        self.type = "button"

        self._mouse_over = False
        surface_images = create_text_element(text,font_size,txt_rgb,bg_rgb)

        bigger_images = create_text_element(text,font_size*1.2,txt_rgb,bg_rgb)

        self.images = [surface_images,bigger_images]
        self.rects = [
            surface_images.get_rect(center=center),
            bigger_images.get_rect(center=center)
        ]
        
        self._action = action

    @property
    def image(self):
        return self.images[1] if self._mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self._mouse_over else self.rects[0]

    #Piirtää update funktion jälkeen.

    def draw(self,surface):

        surface.blit(self.image,self.rect)

    #Update funktio pävitää onko hiiri päällä vai ei.

    def update(self, mouse_pos,surface=None):

        if self.rect.collidepoint(mouse_pos):
            self._mouse_over = True
        else:
            self._mouse_over = False
        if surface:
            self.draw(surface)

    def action(self):
        return self._action

class Element_score(Sprite):
    def __init__(self,center,text,font_size,txt_rgb,bg_rgb):
        super().__init__()
        
        self.type = "score"
        self._font_size = font_size
        self._txt_rgb = txt_rgb
        self._bg_rgb = bg_rgb

        self._mouse_over = False
        surface_images = create_text_element(str(text),font_size,txt_rgb,bg_rgb)

        self.images = [surface_images]
        self.rects = [
            surface_images.get_rect(center=center)
        ]


    @property
    def image(self):
        return self.images[0]

    @property
    def rect(self):
        return self.rects[0]

    def draw(self,surface):

        surface.blit(self.image,self.rect)

    #Päivitää pisteytyksen kun annettu uudet pisteet.

    def update(self,surface=None,score=0):
        self.images[0] = create_text_element(str(score),self._font_size,self._txt_rgb,self._bg_rgb)
        self.draw(surface)

class Element_txt(Sprite):
    def __init__(self,center,text,font_size,txt_rgb,bg_rgb):
        super().__init__()

        self.type = "txt"

        self._mouse_over = False
        surface_images = create_text_element(str(text),font_size,txt_rgb,bg_rgb)

        self.images = [surface_images]
        self.rects = [
            surface_images.get_rect(center=center)
        ]


    @property
    def image(self):
        return self.images[0]

    @property
    def rect(self):
        return self.rects[0]

    def draw(self,surface):

        surface.blit(self.image,self.rect)

    def update(self,surface=None):
        
        if surface:
            self.draw(surface)
