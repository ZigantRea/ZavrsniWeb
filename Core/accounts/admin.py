from django.contrib import admin
from accounts.models import Profil


class ProfilAdmin(admin.ModelAdmin):
    '''
    Registriramo model profila u admin 
    '''
    list_display = ["user", "adresa", "grad", "ime_i_prezime", "datum_rođenja"]


admin.site.register(Profil, ProfilAdmin)
