from django.db import models

class Film(models.Model):
    titre = models.CharField(max_length = 100)
    note = models.IntegerField()
    synopsis = models.TextField(null = True)
    date_sortie = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name="Date de parution")

    def __str__(self):
        return self.titre

