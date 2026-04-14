import pygame

from board import Board
from event_handler import EventQueue
from renderer import Renderer
from game import GameLoop

CELL_SIZE = 50
BOARD_SIZE = 6


def main():
    display_height = CELL_SIZE * BOARD_SIZE
    display_width = CELL_SIZE * BOARD_SIZE
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Blacksmithing")

    pygame.init()

    game = Board(BOARD_SIZE, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, game)

    game.all_sprites.draw(display)

    game_loop = GameLoop(game, renderer, event_queue, CELL_SIZE)
    game_loop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
