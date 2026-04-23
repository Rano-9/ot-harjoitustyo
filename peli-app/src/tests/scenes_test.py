from scenes.board import Board

import unittest

class TestBoardScene(unittest.TestCase):

    def setUp(self):
        self.BOARD_SIZE = 5
        self.CELL_SIZE = 50
        self.FONT_SIZE = 30
        self.TXT_RGB = (255, 0, 0)
        self.BG_RGB = (0, 0, 0)


        self.scenes = {
        "game"  : [Board(self.BOARD_SIZE, self.CELL_SIZE)],
        }
        return super().setUp()

    def test_scenes_inits(self):

        self.assertIsNotNone(self.scenes["game"])
    
    def test_board_scene_function(self):

        id = 0
        num = 1
        allowed = self.scenes["game"][0].get_allowed(id,num)
        self.assertEqual(len(allowed),3)

