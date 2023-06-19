from django.db import models
from categories.models import Category
from genero.models import Genero


# Create your models here.

class Acervo(models.Model):
    name = models.CharField('Titulo', max_length=150)
    year = models.IntegerField('Ano', max_length=4)
    age = models.CharField('Classificacao', max_length=20)
    description = models.TextField('Descricao', max_length=200)
    artist = models.CharField('Artista', max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)
    
    
    class Meta:
        verbose_name = 'Acervo'
        verbose_name_plural = 'Acervos'
        ordering =['id']

    
    @staticmethod
    def cadastrarAcervo (name,year,age,description,artist,category,genero):
        Acervo = Acervo.objects.create(name = Titulo, year = Ano, age = Classificacao, description = Descricao, artist = Artista, category = Category, genero = Genero)
        return Acervo
    
    @staticmethod
    def excluirEspaco (id):
        Acervo = Acervo.objects.get(pk=id)
        Acervo.delete()
        print("deletado com sucesso")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Acervo'
        verbose_name_plural = 'Acervos'
        ordering =['id']
    
    

