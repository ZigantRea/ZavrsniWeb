from django.urls import path
from accounts import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"), #za kreiranje novog usera
    path("create_profil/", views.CreateProfile.as_view(), name="create_profil"), #za kreiranje profila novog usera
    path("profil/<pk>", views.DetailProfile.as_view(), name="profil"), #za prikaz profila
    path("profil-redirect/", views.ProfilRedirect.as_view(), name="profil-redirect"), #ako nema profila da ga proslijedi na kreiranje profila, ako ima onda na prikaz
    path("profil-edit/<pk>", views.EditProfile.as_view(), name="profil-edit"), #za uređivanje profila
]
