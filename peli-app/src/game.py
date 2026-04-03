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
            if event.type == pygame.QUIT or len(self._game.allowed) == 0:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = floor(pos[0]/50)
                y = floor(pos[1]/50)
                tile = self._game.board[x][y]
                if tile in self._game.allowed:
                    num = tile.num
                    loc = tile.location
                    tile.click()
                    print("tile coordinate:",x,y)
                    self._game.get_allowed(num,loc)
                    


            
