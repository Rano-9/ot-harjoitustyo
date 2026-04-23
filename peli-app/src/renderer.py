import pygame


class Renderer:
    def __init__(self, surface, scenes):
        self._surface = surface
        self._scenes = scenes

    def render(self,state,allowed,score):
        mouse_pos = pygame.mouse.get_pos()

        #käydään tilaan liittyvät näkymät
        
        for scene in self._scenes[state]:

            #Katsotaan näkymän tyyppi:

            if scene.type == "menu_scene":

                self._surface.fill((0,0,0))
                scene.surfaces.update(mouse_pos,self._surface)

            #Katsomme näkymä tyypin tai tilan.
            #Koska game tilassa on kaksi näkymää samaan aikaan. 

            elif scene.type == "board_scene" or state == "game":
                if scene.type == "board_scene":
                    allowed = scene.allowed
                    scene.surfaces.update(allowed,self._surface,mouse_pos)

                else:
                    for sprite in scene.surfaces:
                        if sprite.type == "score":
                            sprite.update(self._surface,score)
                        else:
                            sprite.update(self._surface)

            elif scene.type == "score_scene":
                self._surface.fill((0,0,0))
                for sprite in scene.surfaces:
                    if sprite.type == "score":
                        sprite.update(self._surface,score)
                    elif sprite.type == "button":
                        sprite.update(mouse_pos,self._surface)
                    else:
                        sprite.update(self._surface)


        pygame.display.update()
