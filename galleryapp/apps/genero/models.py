from django.db import models

# Create your models here.

class Genero(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering =['id']

    def __str__(self):
        return self.name
