from django import forms
from .models import Napitak, Dodaci


class StavkaForm(forms.Form):
    '''
    Radimo Custom formu jer zelimo da se vidi broj narudžbe ali da ga nije moguce izmjeniti
    '''
    narudzba = forms.CharField(max_length=255, disabled=True) #da ne možemo mijenjati broj narudžbe, da ovo zadnje izbrišemo bi mogli
    napitak = forms.ModelChoiceField(queryset=Napitak.objects.all())
    kolicina = forms.IntegerField()
    toplo = forms.BooleanField(required=False)
    dodatak = forms.ModelMultipleChoiceField(
        queryset=Dodaci.objects.all(), required=False
    )
