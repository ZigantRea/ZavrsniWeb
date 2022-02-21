from django.urls import path
from accounts import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("create_profil/", views.CreateProfile.as_view(), name="create_profil"),
    path("profil/<pk>", views.DetailProfile.as_view(), name="profil"),
    path("profil-redirect/", views.ProfilRedirect.as_view(), name="profil-redirect"),
    path("profil-edit/<pk>", views.EditProfile.as_view(), name="profil-edit"),
]
