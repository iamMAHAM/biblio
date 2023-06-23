from django.forms import ModelForm
from .models import Utilisateur


class RegisterForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'mdp']
