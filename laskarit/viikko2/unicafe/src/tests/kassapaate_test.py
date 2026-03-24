import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
            
    def test_kassa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)

    def test_käteis_syönti_edullinen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(240),0)
        self.assertEqual(self.kassa.edulliset,1)

    def test_käteis_syönti_edullinen_ei_rahaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230),230)
        self.assertEqual(self.kassa.edulliset,0)

    def test_käteis_syönti_maukas(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(400),0)
        self.assertEqual(self.kassa.maukkaat,1)

    def test_käteis_syönti_maukas_ei_rahaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(230),230)
        self.assertEqual(self.kassa.maukkaat,0)

    def test_kortti_syönti_edullinen(self):
        kortti = Maksukortti(240)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti),True)
        self.assertEqual(self.kassa.edulliset,1)

    def test_kortti_syönti_edullinen_ei_rahaa(self):
        kortti = Maksukortti(0)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti),False)
        self.assertEqual(self.kassa.edulliset,0)

    def test_kortti_syönti_maukas(self):
        kortti = Maksukortti(400)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti),True)
        self.assertEqual(self.kassa.maukkaat,1)

    def test_kortti_syönti_maukas_ei_rahaa(self):
        kortti = Maksukortti(0)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti),False)
        self.assertEqual(self.kassa.maukkaat,0)

    def test_saldo_lataus(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti,1000)
        self.assertEqual(kortti.saldo_euroina(),10)
    
    def test_saldo_negatiivinen_lataus(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti,-1000)
        self.assertEqual(kortti.saldo_euroina(),0)
    
    
    
    