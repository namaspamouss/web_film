from django.db import models


class Roles(models.Model):
    role = models.CharField(max_length=100)
    acteur = models.ForeignKey('Acteurs', on_delete=models.CASCADE)
    film = models.ForeignKey('Films', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "role"

    def __str__(self):
        return self.role


class Acteurs(models.Model):
    nom = models.CharField(max_length=100, null = True)
    prenom = models.CharField(max_length=100, null = True)

    class Meta:
        verbose_name = "acteur"

    def __str__(self):
        return self.nom


class Films(models.Model):
    titre = models.CharField(max_length=100, unique=True)
    realisateur= models.CharField(max_length=100, null = True)
    affiche = models.CharField(max_length=200, null = True)
    annee = models.IntegerField(verbose_name="année de sortie", null = True)

    class Meta:
        verbose_name = "film"
        ordering = ['annee']

    def __str__(self):
        return self.titre


