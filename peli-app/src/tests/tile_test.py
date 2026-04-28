from sprites.tile import Tile
import unittest

class TestTile(unittest.TestCase):
    
    def setUp(self):

        self.board_size = 6
        self.tile = Tile((0,0),self.board_size)

        return super().setUp()
    
    def test_tile_inits(self):
        
        self.assertEqual(self.tile.type,"tile")
        self.assertIsNotNone(self.tile.allow)
        self.assertIsNotNone(self.tile.hits)
        self.assertLessEqual(self.tile.num,4)
        self.assertGreater(self.tile.num,0)
        self.assertIsNotNone(self.tile.images)
        self.assertIsNotNone(self.tile.rects)
        
        pass
        

    def test_tile_action(self):
        num = self.tile.num
        output = self.tile.action(self.board_size)

        self.assertEqual(output[1],None)
        self.assertEqual(output[0],num)
        pass    

    