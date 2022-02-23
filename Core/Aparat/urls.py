from django.urls import path
from Aparat import views

urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("narudzba", views.DodajNarudzbu.as_view(), name="dodaj-narudzbu"),
    path("stavka/<pk>", views.DodajStavku.as_view(), name="stavka"),
    path("potvrda/<pk>", views.PotvradaNarudzbe.as_view(), name="potvrda"),
    path("stavka-uredi/<pk>", views.UrediStavku.as_view(), name="stavka-uredi"),
    path("izbrisi/<pk>", views.StavkaIzbrisi.as_view(), name="stavka-izbrisi"),
    path("info-page", views.InfoView.as_view(), name="info"),
    path("dodaj-napitak", views.DodajNapitak.as_view(), name="dodaj-napitak"),
    path("dodaj-dodatak", views.DodajDodatak.as_view(), name="dodaj-dodatak"),
    path("dodaj-salicu", views.DodajSalicu.as_view(), name="dodaj-salicu"),
]
