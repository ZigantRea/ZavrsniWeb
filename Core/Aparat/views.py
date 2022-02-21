from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Aparat.models import Narudzba, Stavka, Dodaci, Napitak, Salica
from accounts.models import Profil
from django.contrib.auth.views import FormView
from Aparat.forms import StavkaForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class Index(TemplateView):
    '''
    View za poćetnu stranicu
    '''
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        '''
        Uzimamo sve napitke i dodatke da ih možemo prikazati kod cijenik na stranici
        '''
        context = super().get_context_data(**kwargs)

        context["napitci"] = Napitak.objects.all()
        context["dodatci"] = Dodaci.objects.all()

        return context


class DodajNarudzbu(CreateView):
    '''
    Defaultni CreateView za narudžbu
    '''
    model = Narudzba
    fields = "__all__"

    def get_success_url(self):
        '''
        Prosljeđujemo na CreateView stavke
        '''
        stavka = Stavka.objects.get(pk=self.kwargs["pk"])
        return reverse("stavka", kwargs={"pk": stavka.narudzba.broj_narudzbe})

    def get_initial(self):
        '''
        Ako logirani korisnik ima profil automatski popunjujemo adresu, grad i ime
        '''
        initial = {}
        if self.request.user.is_authenticated:
            if Profil.objects.filter(user=self.request.user).exists():
                profil = Profil.objects.get(user=self.request.user)
                initial = {
                    "adresa": profil.adresa,
                    "grad": profil.grad,
                    "ime_i_prezime": profil.ime_i_prezime,
                }

        return initial


class DodajStavku(FormView):
    '''
    View za creiranje nove stavke koju automatski vezujemo na kreiranu narudžbu
    '''
    template_name = "Aparat/stavka_form.html"
    form_class = StavkaForm

    def get_initial(self):
        '''
        Vezemo stavku na narudžbu
        '''
        self.pk = Narudzba.objects.get(broj_narudzbe=self.kwargs["pk"])
        initial = {"narudzba": self.pk}
        return initial

    def form_valid(self, form):
        '''
        Spremamo novu kreiranu stavku 
        Moramo u form_valid jer ne koristimo defaultni CreateView
        '''
        narudzba = Narudzba.objects.get(broj_narudzbe=self.kwargs["pk"])
        print(form.cleaned_data["dodatak"])

        stavka = Stavka(
            napitak=form.cleaned_data["napitak"],
            kolicina=form.cleaned_data["kolicina"],
            narudzba=narudzba,
            toplo=form.cleaned_data["toplo"],
        )
        stavka.save()

        for dodatak in form.cleaned_data["dodatak"]:
            d = Dodaci.objects.get(naziv=dodatak)
            print(d)
            stavka.dodatak.add(d)

        stavka.save()

        return super(DodajStavku, self).form_valid(form)

    def get_success_url(self):
        '''
        Nakon sta kreiramo stavku vraca nas ponovno na ovaj view da možemo kreirani novu stavku 
        '''
        return reverse("stavka", kwargs={"pk": self.pk})

    def get_context_data(self, **kwargs):
        '''
        Uzimamo sve stavke s narudžbe da vidimo koje stavke smo vec dodali u narudžbu
        '''
        context = super().get_context_data(**kwargs)

        context["narudzba"] = Narudzba.objects.get(broj_narudzbe=self.kwargs["pk"])

        return context


class PotvradaNarudzbe(DetailView):
    '''
    View za prikaz narudžbe
    Od ovdje možemo prosljedivati na uredivanje stavaka ili brisanje stavaka
    '''
    model = Narudzba


class UrediStavku(UpdateView):
    '''
    View za uredivanje stavke
    '''
    model = Stavka
    template_name = "Aparat/stavka_uredi.html"
    fields = ["napitak", "kolicina", "dodatak"]

    def get_success_url(self):
        '''
        Nakon sto spremimo narudžbu porsljedujemo na potvrud narudzbe
        '''    
        stavka = Stavka.objects.get(pk=self.kwargs["pk"])
        return reverse("potvrda", kwargs={"pk": stavka.narudzba.broj_narudzbe})


class StavkaIzbrisi(DeleteView):
    '''
    View za brisanje stavke 
    '''
    model = Stavka

    def get_success_url(self, **kwargs):
        '''
        Nakon potvrde brisanja prosljedujemo na potvrdu narudžbe
        '''
        stavka = Stavka.objects.get(pk=self.kwargs["pk"])
        return reverse("potvrda", kwargs={"pk": stavka.narudzba.broj_narudzbe})


class InfoView(TemplateView):
    '''
    View za zahvalu nakon potvrde narudžbe
    '''
    template_name = "info.html"


@method_decorator(staff_member_required, name="dispatch")
class DodajNapitak(CreateView):
    '''
    View za dodavanje novog napitka 
    Koristimo method_decorator da samo staff memberi mogu pristupiti (admini)
    '''
    model = Napitak
    fields = "__all__"

    def get_success_url(self):
        '''
        Nakon kreiranja prosljedujemo na profil usera
        '''
        return reverse("profil", kwargs={"pk": self.request.user.pk})


@method_decorator(staff_member_required, name="dispatch")
class DodajDodatak(CreateView):
    '''
    View za dodavanje novog dodatka 
    Koristimo method_decorator da samo staff memberi mogu pristupiti (admini)
    '''
    model = Dodaci
    fields = "__all__"

    def get_success_url(self):
        return reverse("profil", kwargs={"pk": self.request.user.pk})


@method_decorator(staff_member_required, name="dispatch")
class DodajSalicu(CreateView):
    '''
    View za dodavanje novou salicu 
    Koristimo method_decorator da samo staff memberi mogu pristupiti (admini)
    '''
    model = Salica
    fields = "__all__"

    def get_success_url(self):
        return reverse("profil", kwargs={"pk": self.request.user.pk})
