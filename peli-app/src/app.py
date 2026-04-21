import pygame

from board import Board
from event_handler import EventQueue
from renderer import Renderer
from game import GameLoop
from menu import Menu

CELL_SIZE = 50
BOARD_SIZE = 6
FONT_SIZE = 30
TXT_RGB = (255, 0, 0)
BG_RGB = (0, 0, 0)


def main():
    display_height = CELL_SIZE * BOARD_SIZE
    display_width = CELL_SIZE * BOARD_SIZE
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Blacksmithing")

    pygame.init()

    scenes = {
        "start" : Menu((display_height/2,display_width/2),["start","quit"],FONT_SIZE,TXT_RGB,BG_RGB),
        "game" : Board(BOARD_SIZE, CELL_SIZE),
        "score" : Menu((display_height/2,display_width/2),["OUT OF MOVES","QUIT"],FONT_SIZE,TXT_RGB,BG_RGB)
    }
    event_queue = EventQueue()
    renderer = Renderer(display, scenes)

    game_loop = GameLoop(scenes, renderer, event_queue, CELL_SIZE)
    game_loop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
