import pygame

class GameLoop:
    def __init__(self, game, renderer, event_queue, board_size):
        self._scenes = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._board_size = board_size
        self._state = "start"
        self._score = 0


    def _handle_events(self):
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
                pos = pygame.mouse.get_pos()

                #Käydään läpi näykmän elementit
                for element in scene.surfaces:

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
                                record = element.action(self._board_size)
                                allowed = scene.get_allowed(record[1],record[0])
                                self._score += record[0]
                                
                                if not allowed:
                                    self._state = "score"

        if self._state == "quit":
            return False

    def start(self):
        clock = pygame.time.Clock()
        while True:
            if self._handle_events() is False:
                break
            self._renderer.render(self._state,set(),self._score)
            clock.tick(60)
