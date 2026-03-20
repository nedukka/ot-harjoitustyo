import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_rahamaara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_myytyjen_lounaiden_maara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_kateisosto_syo_edullisesti_kasvattaa_kassaa_oikein_maksun_riittaessa(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(300)
        rahamaara = self.kassapaate.kassassa_rahaa
        edullisesti = self.kassapaate.edulliset

        self.assertEqual(rahamaara, 100240)
        self.assertEqual(maksu, 60)
        self.assertEqual(edullisesti, 1)

    def test_kateisosto_syo_maukkaasti_kasvattaa_kassaa_oikein_maksun_riittaessa(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(450)
        rahamaara = self.kassapaate.kassassa_rahaa
        maukkaat = self.kassapaate.maukkaat

        self.assertEqual(rahamaara, 100400)
        self.assertEqual(maksu, 50)
        self.assertEqual(maukkaat, 1)

    def test_kateisosto_syo_edullisesti_ei_kasvata_kassaa_maksun_ei_riittaessa(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(190)
        rahamaara = self.kassapaate.kassassa_rahaa
        edullisesti = self.kassapaate.edulliset

        self.assertEqual(rahamaara, 100000)
        self.assertEqual(maksu, 190)
        self.assertEqual(edullisesti, 0)
    
    def test_kateisosto_syo_maukkaasti_ei_kasvata_kassaa_maksun_ei_riittaessa(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(350)
        rahamaara = self.kassapaate.kassassa_rahaa
        maukkaat = self.kassapaate.maukkaat

        self.assertEqual(rahamaara, 100000)
        self.assertEqual(maksu, 350)
        self.assertEqual(maukkaat, 0)

    def test_kortille_rahaa_ladatessa_saldoa_kassapaatteen_ja_kortin_rahamaara_kasvaa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 900)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100900)
        self.assertEqual(self.maksukortti.saldo, 1900)

    def test_korttiosto_syo_edullisesti_vahentaa_kortin_saldoa_oikein_ja_palauttaa_true_maksun_riittaessa(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(onnistui, True)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_syo_edullisesti_kortin_saldo_oikein_ja_palauttaa_false_maksun_ei_riittaessa(self):
        maksukortti = Maksukortti(100)
        epaonnistui = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(epaonnistui, False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_syo_maukkaasti_vahentaa_kortin_saldoa_oikein_ja_palauttaa_true_maksun_riittaessa(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(onnistui, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_syo_maukkaasti_kortin_saldo_oikein_ja_palauttaa_false_maksun_ei_riittaessa(self):
        maksukortti = Maksukortti(50)
        epaonnistui = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 50)
        self.assertEqual(epaonnistui, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_rahaa_ladatessa_negatiivinen_summa_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -900)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kassapaatteen_rahamaara_euroina_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
