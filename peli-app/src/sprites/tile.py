import os
from random import randint

import pygame

dirname = os.path.dirname(__file__)


class Tile(pygame.sprite.Sprite):
    """
    Luokka UI elementti tile. 
    Muokattu pygame.sprite.sprite luokasta.
    Perii pygame.sprite.sprite ominaisuudet.

    Attributes:
        location: laatan sijainti kentällä
        num: laatan numero joka määrittää seuraavan liikeen
        hits: Kuinka monta kertaa laattaa on isketty
        
        image: laatan pygame.Surface
        rect: laatan pygame.Rect

        allowed: Voiko laattaa klikata
        selected: onko hiiri laatan päällä

    """

    def __init__(self, loc:tuple, board_size:int):
        """
        Laata konstruktori. Luo pygame.sprite.Sprite luokan mukaisen olion:

        Args:
            loc (tuple): Laatan sijainti pelikentällä
            board_size: Pelikentän laattojen lkm rivillä
        
        """
        super().__init__()
        self._id = None
        self._allow = True
        self.__selected = False
        self.__board_size = board_size

        self.location = loc
        self.hits = 0
        self.num = self.__new_num()

        border_path = os.path.join(dirname,"assets","highlight.png")
        selection_path = os.path.join(dirname,"assets","selection.png")
        path = os.path.join(dirname, "assets", "green",f"{self.num}.png") 
        self.__images = [pygame.image.load(path),pygame.image.load(border_path),pygame.image.load(selection_path)]
        self.__rects = [self.__images[0].get_rect(center=loc),self.__images[1].get_rect(center=loc)]

    @property
    def type(self):
        """
        UI elementin tyyppi
            string: "tile"
        """
        return "tile"

    @property
    def rect(self):
        """
        Laatan rect
            pygame.Rect
        """
        return self.__rects[0]

    @property
    def image(self):
        """
        Laatan kuva
            pygame.Surface
        """
        return self.__images[0]

    @image.setter
    def image(self, path):
        self.__images[0] = pygame.image.load(path)

    @property
    def id(self):
        """
        Laatan id numero
            Int
        """
        if self._id is None:
            return None
        return int(self._id)

    @id.setter
    def id(self,value):
        self._id = value

    @property
    def allow(self):
        """
        Voiko laattaa klikata vai ei
            Bool
        """
        return self._allow

    @allow.setter
    def allow(self,value:bool):
        self._allow = value

    #Piirtää sen mukaan mitä update funktio asetti arvoja
    #Images 1 on korostus reunus 2 valinta reunus.

    def draw(self,surface:pygame.Surface):
        """
        Laatan piirto funktio.

        Käytä laatan update funktiota laatan piirtämiseen:
        """

        surface.blit(self.image,self.rect)

        if self.__selected:
            surface.blit(self.__images[2],self.rect)
        elif self._allow:
            surface.blit(self.__images[1],self.rect)


    # Update funktio joka luo korostetuun reunukseen laatalle.

    def update(self, allowed:set,surface:pygame.Surface=None,pos:tuple=(-1,-1)):
        """
        Laatan päivitys funktio.

        Args:
            allowed: Lista sallituista laatoista
            surface: pygame.Surface alusta johon elementti piirretään
            pos: Hiiren sijainti
        
        """
        if self.id in allowed and self.hits < 3:

            self.allow = True
            if self.rect.collidepoint(pos):
                self.__selected = True
            else:
                self.__selected = False
        else:
            self._allow = False
            self.__selected = False


        if surface:
            self.draw(surface)


    #Elementin oma action. Kun on hiiri kohdallaan lasketaan uusi numero.
    #Kuvake muuttuu numeron ja osumien mukaan.

    def action(self):
        """
        Laatan action funktio

        Päivittää laatan iskut ja kuvan kun laattaa klikataan

        """
        prev = self.num

        self.num = self.__new_num()
        path = None
        self.hits += 1

        match self.hits:
            case 0:
                color = "green"
                path = os.path.join(dirname, "assets",
                                    color, f"{self.num}.png")
            case 1:
                color = "yellow"
                path = os.path.join(dirname, "assets",
                                    color, f"{self.num}.png")
            case 2:
                color = "red"
                path = os.path.join(dirname, "assets",
                                    color, f"{self.num}.png")
            case 3:
                self.image.fill((0, 0, 0))

        if path is not None:
            self.image = path

        return (prev, self.id)

    def __new_num(self):
        """
        Antaa laatalle uuden numeron
        """
        x , y = self.location

        num = randint(1, 4)

        if int(x/50) + num >= self.__board_size  and int(y/50) + num >= self.__board_size and int(x/50) - num < 0 and int(y/50) - num < 0:
            num =randint(1,3)

        return num
