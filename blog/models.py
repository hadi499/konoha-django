from django.db import models


class Shinobi(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name
