from sprites.tile import Tile
import unittest

class TestTile(unittest.TestCase):
    
    def setUp(self):
        self.tile = Tile()

        return super().setUp()
    
    def test_tile_inits(self):
        #Laattaa on klikattu ensimmäisen kerran
        self.assertEqual(self.tile.hits,1)

        #Laatalla on numero
        self.assertIsNotNone(self.tile.num)

        #Numero on 1 ja 4 välissä
        self.assertLessEqual(self.tile.num,4)
        self.assertGreaterEqual(self.tile.num,1)
    
    def test_tile_clicks(self):

        #Kun laattaa painetaan painallukset nousee
        self.assertEqual(self.tile.hits,1)
        self.tile.click()
        self.assertEqual(self.tile.hits,2)

        #Jos voisi testata satunnaisuutta testaisin

    
