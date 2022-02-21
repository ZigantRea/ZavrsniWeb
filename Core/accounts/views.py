from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from accounts.models import Profil
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.views.generic import RedirectView


class SignUpView(CreateView):
    '''
    View za registraciju novih korisnika. Koristimo "django.contrib.auth" paket za registraciju
    '''
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CreateProfile(LoginRequiredMixin, CreateView):
    '''
    View za creiranje novog profile, LoginRequiredMixin da samo legirani korsinici mogu pristupiti
    '''
    model = Profil
    fields = ["adresa", "grad", "ime_i_prezime", "datum_rođenja"]
    success_url = "/"

    def form_valid(self, form):
        '''
        Koristimo da profil zadamo trenutno registriranom korisniku
        '''
        item = form.save()
        item.user = self.request.user
        return super(CreateProfile, self).form_valid(form)


class DetailProfile(LoginRequiredMixin, DetailView):
    '''
    View za prikaz profila, LoginRequiredMixin da samo legirani korsinici mogu pristupiti
    '''
    model = Profil


class EditProfile(LoginRequiredMixin, UpdateView):
    '''
    View za uređivanje profila, LoginRequiredMixin da samo legirani korsinici mogu pristupiti
    '''
    model = Profil
    fields = ["adresa", "grad", "ime_i_prezime", "datum_rođenja"]

    def get_success_url(self):
        '''
        Pokrece se da se nakon promjena profila vratimo na prikaz profila logiranog korinika
        '''
        return reverse("profil", kwargs={"pk": self.request.user.pk})


class ProfilRedirect(RedirectView):
    '''
    Ako korinsik jos nema porfil preusmjerava ga na izradu porfila ako ima preusmjerava ga na pregled profila
    '''
    def get_redirect_url(self):
        if Profil.objects.filter(user=self.request.user).exists():
            return reverse("profil", kwargs={"pk": self.request.user.pk})

        else:
            return reverse("create_profil")
