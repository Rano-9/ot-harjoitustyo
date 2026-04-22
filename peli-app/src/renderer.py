import pygame


class Renderer:
    def __init__(self, surface, scenes):
        self._surface = surface
        self._scenes = scenes

    def render(self,state,allowed,score):
        mouse_pos = pygame.mouse.get_pos()
        for scene in self._scenes[state]:
            if state == "start":

                self._surface.fill((0,0,0))
                scene.surfaces.update(mouse_pos,self._surface)

            elif state == "game":
                if scene.type == "board":
                    allowed = scene.allowed
                    scene.surfaces.update(allowed,self._surface,mouse_pos)

                else:
                    scene.surfaces.update(allowed,self._surface,mouse_pos)

            elif state == "score":
                self._surface.fill((0,0,0))
                scene.surfaces.update(mouse_pos,self._surface)


        pygame.display.update()
