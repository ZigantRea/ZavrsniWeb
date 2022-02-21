from django.contrib import admin


from Aparat.models import Napitak, Narudzba, Dodaci, Salica, Stavka


'''
Rekistriramo sve modele u admin
'''

class NapitakAdmin(admin.ModelAdmin):
    pass


admin.site.register(Napitak, NapitakAdmin)


class StavkaAdminInline(admin.TabularInline):
    '''
    Klasa za inlines u NarudzbaAdmin
    '''
    model = Stavka


class NarudzbaAdmin(admin.ModelAdmin):
    '''
    Koristimo inlines da se ispod narudžba prikaze sve stavke vezane za tu narudžbu
    '''
    inlines = (StavkaAdminInline,)
    list_display = ("broj_narudzbe", "vrijeme_kupnje", "ukupna_cijena")


admin.site.register(Narudzba, NarudzbaAdmin)


class DodaciAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dodaci, DodaciAdmin)


class SalicaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Salica, SalicaAdmin)


class StavkaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stavka, StavkaAdmin)
