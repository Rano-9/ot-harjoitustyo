import pygame

class GameLoop:
    def __init__(self, game, renderer, event_queue, size):
        self._scenes = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._size = size
        self._state = "start"
        self._score = 0


    def _handle_events(self):
        pos = None
        click = False

        #Katsotaan oliko eventtejä
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONUP:
                click = True
                if self._state == "score":
                    return False

        #Jos oli tehdään jotain
        if click:
            for scene in self._scenes[self._state]:
                pos = pygame.mouse.get_pos()

                for surface in scene.surfaces:
                    if surface.rect.collidepoint(pos):
                        if self._state == "start":
                            self._state = surface.action()

                        elif self._state == "game":
                            if surface.allow and surface.hits < 4:
                                record = surface.click()
                                allowed = scene.get_allowed(record[1],record[0])
                                self._score += record[0]
                                scene.surfaces.update(allowed,self._renderer._surface)

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
