import pygame


class Renderer:
    def __init__(self, surface, scenes):
        self._surface = surface
        self._scenes = scenes

    def render(self,state):
        mouse_pos = pygame.mouse.get_pos()
        if state == "start":
            
            self._surface.fill((0,0,0))
            self._scenes["start"].text_surfaces.update(mouse_pos)
            self._scenes["start"].text_surfaces.draw(self._surface)
        
        if state == "game":
            self._scenes["game"].all_sprites.draw(self._surface)

        pygame.display.update()
