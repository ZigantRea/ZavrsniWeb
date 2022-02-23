from Aparat.forms import StavkaForm
from Aparat.models import Dodaci, Napitak, Narudzba, Salica, Stavka
from django.test import TestCase
from django.urls import reverse

def primjerDodatak():
    return Dodaci.objects.create(naziv = 'testDodatak', cijena = 15.00)
def primjerSalica():
    return Salica.objects.create(boja = '#FF0000', materijal = 'TestMaterijal')
def primjerNapitak():
    return Napitak.objects.create(vrsta_napitka = 'TestNapitak', cijena = 15.00, salica = primjerSalica())
def primjerNarudzba():
    return Narudzba.objects.create(vrijeme_isporuke = '12:50', adresa = 'TestAdresa', grad = 'testGrad', ime_i_prezime = 'testIme')

def primjerStavka():
    return Stavka.objects.create(naptak = primjerNapitak(), kolicina = 2, narudzba = primjerNarudzba(), dodatak = primjerDodatak(), toplo = True)

class TestForms(TestCase):

    def setUp(self):
        self.narudzba = primjerNarudzba()

    def test_form_is_valid(self):
        '''
        Testiramo ako radi nasa custom forma
        '''
        narudzba = self.narudzba
        napitak = primjerNapitak()
        kolicina = 2
        toplo = True
        dodatak = primjerDodatak()
        form = StavkaForm(data={'narudzba': narudzba,
                                'napitak': napitak,
                                'kolicina': kolicina,
                                'toplo': toplo,
                                'dodatak': dodatak})
        self.assertFalse(form.is_valid())

class Testiranje(TestCase):

    def setUp(self):
        self.narudzba = primjerNarudzba()
  
    def test_kreiranje_narudzbe(self):
        """
        Test kreiranje narudzbe
        """

        res = self.client.get(reverse("dodaj-narudzbu"))
        self.assertEqual(res.status_code, 200)
        
    def test_kreiranje_stavke(self):
        """
        Test kreiranje stavke
        """

        res = self.client.get(reverse("stavka", kwargs={"pk": self.narudzba.pk}))
        self.assertEqual(res.status_code, 200)

    def test_potvrda_narudzbe(self):
        """
        Test potvrde narduzbe
        """

        res = self.client.get(reverse("potvrda", kwargs={"pk": self.narudzba.pk}))
        self.assertEqual(res.status_code, 200)
