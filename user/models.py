from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True)
    mdp = models.CharField(max_length=50)
    # generer un champ de date de creation avec pou valeur par defaut le timestamp actuel
    date_de_creation = models.DateTimeField(auto_now_add=True)
    date_de_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    date_de_creation = models.DateTimeField(auto_now_add=True)
    date_de_mise_a_jour = models.DateTimeField(auto_now=True)
