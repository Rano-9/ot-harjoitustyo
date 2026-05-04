import pygame
from math import floor

from sprites.tile import Tile



class Board:
    """
    Luokka joka käsittelee Board näkymän elementtejä

    Attributes:
        type: Näkymän tyyppi (board_scene).
        surfaces: Sprite group joka sisältää luokan elementit

    """


    def __init__(self, board_size:int, cell_size:int):
        """
        Luokan konstruktori, luo uuden näkymän

        Args:
            board_size: Kuinka monta laattaa kentällä on
            cell_size: Kuinka suuri yksi laatta on
        """

        self.surfaces = pygame.sprite.Group()
        self.__tiles = []
        self.__board_size = board_size
        self.__allowed = set()

        # Luodaan peliin laatat.
        # Käydään läpi pelikentän koko. Kenttä on n²
        # Luodaan jokaiselle kohdalle laatta.
        # Laatan keskipiste lasketaan laatan koosta.

        for i in range(self.__board_size):
            for j in range(self.__board_size):
                x = cell_size/2
                y = cell_size/2
                coord = (x + j*cell_size,y + i*cell_size)
                tile = Tile(coord,self.__board_size)
                self.__tiles.append(tile)
                tile.id = len(self.__tiles)-1

                self.__allowed.add(tile.id)
                self.surfaces.add(tile)

    @property
    def allowed(self):
        """
        Allowed setin getter
        
        Returns:
            set(): Sallitujen laattojen joukko
        """

        return self.__allowed

    def get_allowed(self, id,num):
        """
        Allowed joukon päivittäjä

        Args:
            id: Viimeksi käydyn laatan id
            num: Viimeksi käydyn laatan numero
        
        Return: 
            Allowed_set: Sallittujen laattojen joukko
        """


        self.__allowed.clear()

        col = id % self.__board_size
        row = floor(id / self.__board_size)

        # Käydään läpi 9x9 gridi ja lisätään laatat jotka ovat gridin sisällä
        # Ei lisätä laattaa gridin keskellä

        for i in range(-1,2):
            for j in range(-1,2):
                pos_x = col + (i*num)
                if pos_x < self.__board_size and pos_x >=0:
                    pos_y = row + (j*num)
                    if pos_y < self.__board_size and pos_y >=0:
                        pos = pos_y * self.__board_size + pos_x
                        if pos != id and self.__tiles[pos].hits < 3:
                            self.__allowed.add(pos)


        return self.__allowed



    @property
    def type(self):
        """
        Luokan tyyppi getter

        Returns:
            "board_scene"
        """

        return "board_scene"