import pygame

from sprites.tile import Tile



class Board:
    def __init__(self, board_size, cell_size):
        self.size = cell_size
        self.board_size = board_size
        self.board = []
        self.tiles = pygame.sprite.Group()
        self.allowed = set()
        index = 0
        for i in range(board_size):
            row = []
            for j in range(board_size):
                tile = Tile((i, j))
                index += 1
                row.append(tile)
                self.allowed.add(tile)
            self.board.append(row)

        #States are star, game, score, end
        self.state = "start"
        
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
    
    def get_allowed(self, tile):
        self.allowed.clear()

        num, loc = tile
        # käydään kohteet läpi x akselin -1 0 1 suhteessa iskettyyn numeroon
        for i in range(-1, 2):
            # ratkaistaan x
            x = loc[0] + num*i
            if x >= 0 and x < self.board_size:

                # Käydään sama mutta y akseli
                for j in range(-1, 2):
                    # ratkaistaan y
                    y = loc[1] + num*j
                    if y >= 0 and (x, y) != loc and y < self.board_size:
                        tile = self.board[x][y]
                        if tile.hits < 4:
                            self.allowed.add(tile)
                            print("next tile coordinate", x, y)
