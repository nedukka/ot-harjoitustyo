import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(325)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 13.25 euroa")   

    def test_rahaa_ottaessa_saldo_vahenee_oiken_jos_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(600)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 4.00 euroa")

    def test_rahaa_ottaessa_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1400)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahaa_ottaessa_paluuarvo_true_jos_tarpeeksi_rahaa_muuten_false(self):
        saldo_riittaa = self.maksukortti.ota_rahaa(600)
        saldo_ei_riita = self.maksukortti.ota_rahaa(1400)

        self.assertEqual((saldo_riittaa, saldo_ei_riita), (True, False))

    def test_kortin_saldo_euroina_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)