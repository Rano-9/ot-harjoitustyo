import pygame


class Renderer:
    def __init__(self, surface, scenes):
        self._surface = surface
        self._scenes = scenes

    def render(self,state,allowed):
        mouse_pos = pygame.mouse.get_pos()
        if state == "start":

            self._surface.fill((0,0,0))
            self._scenes["start"].surfaces.update(mouse_pos,self._surface)

        elif state == "game":
            self._scenes["game"].surfaces.update(allowed,self._surface,mouse_pos)

        elif state == "score":
            self._surface.fill((0,0,0))
            self._scenes["score"].surfaces.update(mouse_pos,self._surface)

        pygame.display.update()
