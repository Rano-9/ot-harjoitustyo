import pygame
from math import floor

class GameLoop:
    def __init__(self, game,renderer, event_queue, size):
        self._game  = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._size = size
        
    def start(self):
        clock = pygame.time.Clock()
        while True:
            if self._handle_events() == False:
                break
            self._renderer.render()
            clock.tick(60)
            
    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self._game.board[floor(pos[0]/50)][floor(pos[1]/50)].click()

            if event.type == pygame.QUIT:
                return False