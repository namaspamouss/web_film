from django.db import models
from django.utils import timezone

class Article(models.Model):
    nom = models.CharField(max_length=40)
    image = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    type_ = models.CharField(max_length=10)

    class Meta:
        verbose_name = "article"

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom = models.CharField(max_length=40)

    class Meta:
        verbose_name = "categorie"

    def __str__(self):
        return self.nom


class Commande(models.Model):
    date = models.DateTimeField(verbose_name="date de sortie")
    #client = 
    montant = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "commande"

    def __str__(self):
        return self.date


class Ligne_de_commande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=3)

    class Meta:
        verbose_name = "panier"

    def __str__(self):
        return self.commande