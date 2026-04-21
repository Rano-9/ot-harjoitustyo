import pygame

from sprites.tile import Tile



class Board:
    def __init__(self, board_size, cell_size):
        self.size = cell_size
        self.board_size = board_size
        self.surfaces = pygame.sprite.Group()
        self.allowed = set()
        index = 0
        for i in range(board_size):
            row = []
            for j in range(board_size):
                x = cell_size/2
                y = cell_size/2
                coord = (x + i*cell_size,y + j*cell_size)
                tile = Tile(index,coord)
                tile.id = index
                index += 1
                self.allowed.add(index)
                self.surfaces.add(tile)

        #States are star, game, score, end
    
    def get_allowed(self, tile):
        self.allowed.clear()
