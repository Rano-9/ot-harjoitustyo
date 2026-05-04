import pygame

from scenes.board import Board
from scenes.menu import Menu
from scenes.score import Score

import sprites.elements as elements
import sprites.tile as tile


class GameLoop:
    """
    Pelilooppi luokka.

    Luokka huolehtii että peli käynnistyy ja huolehtii eventtien käsittelystä.
    """

    def __init__(self, scenes:dict, renderer, event_handler, board_size):
        """
        Peliloopin konstruktori.

        Args:
            Scenes: Dict olio joka sisältää pelin näkymät
            
            Renderer: Pelin renderöijä olio
            
            Event_handler: Peli event hakija

            Board_size: Pelikentän yhden rivin leveys 
            määrittää pelikentän koon
        """

        self._scenes = scenes
        self._renderer = renderer
        self._event_queue = event_handler
        self._board_size = board_size
        self._state = "start"
        self._score = 0


    def _handle_events(self):
        """
        Peliloopin eventtien käsittely funktio
        
        Hakee tapahtuneet eventit ja käy niitä lävitse
        """

        pos = None
        click = False

        #Katsotaan oliko eventtejä jonossa
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONUP:
                click = True
                if self._state == "score":
                    return False

        #Jos oli tehdään jotain
        if click:

            #Käydään läpi jokainen näkymä joka on nykyisessä tilanteessa.
            for scene in self._scenes[self._state]:
                scene:Board|Score|Menu
                pos = pygame.mouse.get_pos()

                #Käydään läpi näykmän elementit
                for element in scene.surfaces:
                    element: tile.Tile|elements.Element_button|elements.Element_score|elements.Element_txt

                    #Katsotaan onko hiiri päällä, jos ei ole skipataan listassa.

                    if element.rect.collidepoint(pos):

                        #Katsotaan mikä on elementin typpi
                        #Tile ja Button elementeillä on action
                        #Muilla elementeillä ei ole actioniä

                        if element.type == "button":
                            self._state = element.action()

                        elif element.type == "tile":

                            # Tarkistetaan voidaanko klikata

                            if element.allow and element.hits < 3:
                                record = element.action()
                                allowed = scene.get_allowed(record[1],record[0])
                                self._score += record[0]

                                if not allowed:
                                    self._state = "score"

        if self._state == "quit":
            return False
        return True

    def start(self):
        """
        Peliloopin aloitus funktio
        """
        clock = pygame.time.Clock()
        while True:
            if self._handle_events() is False:
                break
            self._renderer.render(self._state,set(),self._score)
            clock.tick(60)
