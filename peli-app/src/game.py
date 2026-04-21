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
        for event in self._event_queue.get():
            click = False
            if event.type == pygame.QUIT:
                return None

            if self._state == "game":
                if not self._scenes["game"].allowed:
                    print(self._scenes["game"].allowed)
                    self._state = "score"

            if event.type == pygame.MOUSEBUTTONUP:
                click = True
                pos = pygame.mouse.get_pos()
                x = floor(pos[0]/50)
                y = floor(pos[1]/50)
                if self._state == "start":
                    if self._scenes["start"].text_surfaces.collidepoint(pos):
                        self._state = "game"
                    

                elif self._state == "game":
                    tile = self._scenes["game"].board[x][y]
                    if tile in self._scenes["game"].allowed:
                        print("tile coordinate:", x, y)
                        self._scenes["game"].get_allowed(tile.click())
                    return None


    def start(self):
        clock = pygame.time.Clock()
        while True:
            if self._handle_events() is False:
                break
            self._renderer.render(self._state)
            clock.tick(60)
