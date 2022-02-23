from django.db import models
from django.contrib.auth import get_user_model


class Profil(models.Model):
    '''
    Proširujemo defaultni user model sa OneToOne modelom
    Koristimo OneToOne model jer nismo uredili defaultnog usera prije prve migracije
    '''
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    adresa = models.CharField(blank=True, max_length=255, null=True)
    grad = models.CharField(blank=True, max_length=255, null=True)
    ime_i_prezime = models.CharField(blank=True, max_length=255, null=True)
    datum_rođenja = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ime_i_prezime
