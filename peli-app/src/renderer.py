import pygame


class Renderer:
    def __init__(self, surface, board):
        self._surface = surface
        self._board = board

    def render(self):
        self._board.all_sprites.draw(self._surface)

        pygame.display.update()
