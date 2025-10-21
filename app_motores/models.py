from django.db import models

class Motor(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f'Motor: {self.marca} {self.modelo}'
