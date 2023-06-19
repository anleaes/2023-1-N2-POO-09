from django.db import models

# Create your models here.

class Category(models.Model):
    
    name = models.CharField('Titulo', max_length=100)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name