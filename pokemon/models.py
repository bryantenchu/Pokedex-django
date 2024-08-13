# pokemon/models.py

from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    image_url = models.URLField()
    weight = models.FloatField()
    height = models.FloatField()
    abilities = models.TextField()
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
