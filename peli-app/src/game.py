from math import floor

import pygame

class GameLoop:
    def __init__(self, game, renderer, event_queue, size):
        self._scenes = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._size = size
        self._state = "start"


    def _handle_events(self):
        pos = None
        click = False
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONUP:
                click = True
                pos = pygame.mouse.get_pos()
                
        
        for i in self._scenes[self._state].surfaces:
            if click:
                pos = pygame.mouse.get_pos()
                if i.rect.collidepoint(pos):
                    if self._state == "start":
                        self._state = "game"

                    elif self._state == "game":
                        if i.allow and i.hits < 4:
                            record = i.click()
                            allowed = self._scenes[self._state].get_allowed(record[1],record[0])

                            self._scenes[self._state].surfaces.update(allowed,self._renderer._surface)

        if self._state == "game":
            if not self._scenes[self._state].allowed:
                return False

    def start(self):
        clock = pygame.time.Clock()
        while True:
            if self._state == "game":
                allowed = self._scenes[self._state].allowed
            else:
                allowed = set()
            if self._handle_events() is False:
                break
            self._renderer.render(self._state,allowed)
            clock.tick(60)
