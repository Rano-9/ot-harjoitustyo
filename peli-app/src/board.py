from sprites.tile import Tile
import pygame

class Board:
    def __init__(self, board_size,cell_size):
        self.size = cell_size
        self.board_size = board_size
        self.board  = []
        self.tiles = pygame.sprite.Group()
        index = 0
        for i in range(board_size):
            row = []
            for j in range(board_size):
                tile = Tile(i,j, index)
                index += 1
                row.append(tile)
            self.board.append(row)

        self.all_sprites = pygame.sprite.Group()
        self._init_sprites()

    def _init_sprites(self):
        for x in range(self.board_size):
            for y in range(self.board_size):

                cell = self.board[x][y]
                cell.rect.x = x*self.size
                cell.rect.y = y*self.size
                
                self.tiles.add(cell)
                
        self.all_sprites.add(self.tiles)