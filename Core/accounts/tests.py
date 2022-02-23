from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client
from accounts.models import Profil

class KorisnikTest(TestCase):
    """
    Testiramo korinsnike
    """
    def setUp(self):
        self.client = Client()
        username = 'test'
        email = 'test@test.com'
        password = 'Testpass123'
        self.korisnik = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

    def test_napravimo_novog_korisnika(self):
        """
        Testiranje izrada novog korisnika
        """
        username = 'normal'
        email = 'normal@test.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_bez_username(self):
        """
        Testiramo zadovaljvanje kriterija za kreiranje korisnika
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@test.com', 'test123')

    def test_samo_logirani_korisnici_pristupaju_detail(self):
        """
        Testoramo da samo logirani korisnici mogu pristupiti detail profil stranici
        """

        res = self.client.get(reverse("profil-redirect"))
        self.assertEqual(res.status_code, 302)
    
    def test_kao_logirani_na_profilu(self):
        """
        Testiramo kao logirani korisnik
        """
        Profil.objects.create(user = self.korisnik, adresa = 'test', grad = 'test', ime_i_prezime= 'test', datum_rođenja = '1999-12-12')
        self.client.login(username = 'test', password = 'Testpass123')

        res = self.client.get(reverse("profil-redirect"))
        #print(res)
        self.assertEqual(res.status_code, 302)
