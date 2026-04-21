import pygame
import pygame.freetype
from pygame.sprite import Sprite


def create_menu_text(text, font_size, txt_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=txt_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class Element_button(Sprite):
    def __init__(self,center,text,font_size,txt_rgb,bg_rgb):
        super().__init__()

        self._mouse_over = False
        surface_images = create_menu_text(text,font_size,txt_rgb,bg_rgb)
        
        bigger_images = create_menu_text(text,font_size*1.2,txt_rgb,bg_rgb)
        
        self.images = [surface_images,bigger_images]
        self.rects = [
            surface_images.get_rect(center=center),
            bigger_images.get_rect(center=center)
        ]
        self.state = "start"

    @property
    def image(self):
        return self.images[1] if self._mouse_over else self.images[0]
    
    @property
    def rect(self):
        return self.rects[1] if self._mouse_over else self.rects[0]
    
    def draw(self,surface):
    
        surface.blit(self.image,self.rect)
    
    def update(self, mouse_pos,surface):

        if self.rect.collidepoint(mouse_pos):
            self._mouse_over = True
        else:
            self._mouse_over = False

        self.draw(surface)