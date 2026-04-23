import pygame
from math import floor

from sprites.tile import Tile



class Board:
    def __init__(self, board_size, cell_size):
        self.type = "board_scene"

        self.surfaces = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.tiles = []

        self.size = cell_size
        self.board_size = board_size
        self.allowed = set()
        

        
        for i in range(board_size):
            for j in range(board_size):
                x = cell_size/2
                y = cell_size/2
                coord = (x + j*cell_size,y + i*cell_size)
                tile = Tile(coord,board_size)
                self.tiles.append(tile)
                tile.id = len(self.tiles)-1

                self.allowed.add(tile.id)
                self.surfaces.add(tile)

    def get_allowed(self, id,num):
        self.allowed.clear()

        col = id % self.board_size
        row = floor(id / self.board_size)

        for i in range(-1,2):
            for j in range(-1,2):
                pos_x = col + (i*num)
                if pos_x < self.board_size and pos_x >=0:
                    pos_y = row + (j*num)
                    if pos_y < self.board_size and pos_y >=0:
                        pos = pos_y * self.board_size + pos_x
                        if pos != id and self.tiles[pos].hits < 3:
                            self.allowed.add(pos)


        return self.allowed

