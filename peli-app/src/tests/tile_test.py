from sprites.tile import Tile
import unittest

class TestTile(unittest.TestCase):
    
    def setUp(self):

        self.tile = Tile((0,0))

        return super().setUp()
    
    def test_tile_inits(self):
        
        self.assertIsNotNone(self.tile.allow)
        self.assertIsNotNone(self.tile.hits)
        self.assertLessEqual(self.tile.num,4)
        self.assertGreater(self.tile.num,0)
        self.assertIsNotNone(self.tile.images)
        self.assertIsNotNone(self.tile.rects)
        
        pass
        

    def test_tile_clicks(self):
        num = self.tile.num
        output = self.tile.click()

        self.assertEqual(output[1],None)
        self.assertEqual(output[0],num)
        pass    
