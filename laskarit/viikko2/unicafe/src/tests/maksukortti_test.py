import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_tulostus_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    
    def test_kortin_saldo_kasvaa(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11)
    
    def test_kortin_saldo_muuttuu_nostossa(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(self.maksukortti.saldo_euroina(), 1)
    

    def test_kortin_saldo_ei_muuttu_ylinostossa(self):
        self.maksukortti.ota_rahaa(9000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)