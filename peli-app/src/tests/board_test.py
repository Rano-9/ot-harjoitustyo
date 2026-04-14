from board import Board
import unittest

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.BOARD_SIZE = 5
        self.CELL_SIZE = 50
        self.board = Board(self.BOARD_SIZE,self.CELL_SIZE)
        return super().setUp()
    
    def test_board_inits(self):
        
        #Testataan sisältääkö kenttä luokka listan kooltaan BOARD_SIZE
        self.assertEqual(len(self.board.board),self.BOARD_SIZE )

        #Testataan kaikki kentän laatat on käytettävissä eli BOARD_SIZE * BOARD_SIZE
        self.assertEqual(len(self.board.allowed),(self.BOARD_SIZE*self.BOARD_SIZE))
        
    def test_board_tile_hits(self):
        
        #Testatan että voidaan käyttää kentän laattoja
        tile = self.board.board[0][0]
        tile.click()
        self.assertGreater(tile.hits,1)
        
    def test_board_gives_correct_tiles(self):

        #Haetaan uudet sallitut laatat kun ollaan teknisesti painettu ensimmäistä

        self.board.get_allowed((1,(0,0)))

        testTile = self.board.board[1][0]
        self.assertIn(testTile,self.board.allowed)

        testTile = self.board.board[0][1]
        self.assertIn(testTile,self.board.allowed)
        
        testTile = self.board.board[1][1]
        self.assertIn(testTile,self.board.allowed)
        
        