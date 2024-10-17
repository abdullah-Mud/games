from django.db import models 

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description