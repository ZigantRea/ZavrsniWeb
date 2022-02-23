from django.db import models
from colorfield.fields import ColorField
import uuid


'''
Izrađujemo modele 
verbose_name i verbose_name_plural koristimo za točan ispis naziva modela u adminu
__str__ za ljudiski citljiv ispis kad pozovemo samo objekt modela
'''
class Salica(models.Model):
    boja = ColorField(default="#FF0000")
    materijal = models.CharField(max_length=255)

    def __str__(self):
        return f"{ self.materijal } -- { self.boja }"

    class Meta:
        verbose_name = "Šalica"
        verbose_name_plural = "Šalice"


class Dodaci(models.Model):
    naziv = models.CharField(max_length=255, unique=True)
    cijena = models.DecimalField(max_digits=6, decimal_places=2)
    slika = models.ImageField(upload_to="dodaci/", default="default_dodaci.jpg")

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = "Dodatak"
        verbose_name_plural = "Dodaci" #kako će mi biti prikazano u adminu tao lijevo lijepo


class Napitak(models.Model):
    vrsta_napitka = models.CharField(max_length=255, unique=True)
    cijena = models.DecimalField(max_digits=6, decimal_places=2)
    salica = models.ForeignKey(Salica, on_delete=models.CASCADE)
    slika = models.ImageField(upload_to="pica/", default="default_drink.jpg")

    def __str__(self):
        return self.vrsta_napitka

    class Meta:
        verbose_name = "Napitci"
        verbose_name_plural = "Napitak"


class Narudzba(models.Model):
    '''
    broj_narudžbe automatski dodjeljijemo autogenerirani kod i postavaljamo ga kao primary key
    '''
    broj_narudzbe = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    vrijeme_kupnje = models.DateTimeField(auto_now_add=True, editable=False)
    vrijeme_isporuke = models.TimeField(null=True)
    adresa = models.CharField(max_length=255, null=True)
    grad = models.CharField(max_length=255, null=True)
    ime_i_prezime = models.CharField(max_length=255, null=True)

    '''
    Koristimo property da mozemo izvršiti matematicku akciju prije ispisa polja (sumu svih cijena)
    '''
    @property
    def ukupna_cijena(self):
        stavke = self.stavke.all()
        sum = 0
        for s in stavke:
            sum = sum + s.cijena
        return sum

    def __str__(self):
        return str(self.broj_narudzbe)

    class Meta:
        verbose_name = "Narudžba"
        verbose_name_plural = "Narudžbe"


class Stavka(models.Model):
    napitak = models.ForeignKey(Napitak, on_delete=models.CASCADE)
    kolicina = models.IntegerField()
    narudzba = models.ForeignKey(
        Narudzba, on_delete=models.CASCADE, related_name="stavke"
    )
    dodatak = models.ManyToManyField(Dodaci, blank=True)
    toplo = models.BooleanField(default=True)

    '''
    Koristimo property da mozemo izvršiti matematicku akciju prije ispisa polja (sumu svih cijena)
    '''
    @property
    def cijena(self):
        sum = self.napitak.cijena * self.kolicina

        for d in self.dodatak.all():
            sum = sum + d.cijena
        return sum

    def __str__(self):
        return self.napitak.vrsta_napitka

    class Meta:
        verbose_name = "Stavka"
        verbose_name_plural = "Stavke"


class DodatakStavka(models.Model):
    '''
    Pomoćni model za Dodatak i stavku ManyToMany relaciju
    '''
    napitak = models.ForeignKey(Stavka, on_delete=models.CASCADE)
    dodatak = models.ForeignKey(Dodaci, on_delete=models.CASCADE)
