import unittest

import pygame

from sprites.elements import Element_button
from sprites.elements import Element_txt
from sprites.elements import Element_score


class TestTile(unittest.TestCase):
    
    def setUp(self):
        pygame.freetype.init()
        pygame.display.init()
        pygame.display.set_mode((1,1))

        self.button = Element_button((0,0),"button",50,(0,0,0),(0,0,0))
        self.txt_element = Element_txt((0,0),"text",50,(0,0,0),(0,0,0))
        self.score_element = Element_score((0,0),"Score",50,(0,0,0),(0,0,0))


        return super().setUp()
    
    def test_elements_init(self):
        
        self.assertEqual(self.button.type, "button")
        self.assertEqual(self.txt_element.type, "txt")
        self.assertEqual(self.score_element.type, "score")
        
        
        pass