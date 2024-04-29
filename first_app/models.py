from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    def __str__(self):
        return self.name 