from django.db import models
from exposicoes.models import Exposicao
from pessoas.models import Pessoa

# Create your models here.
class Ingresso (models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    exposicao = models.ForeignKey(Exposicao, on_delete=models.CASCADE)

    @staticmethod
    def cadastraringresso(pessoa, exposicao):
        ingresso = Ingresso.objects.create(pessoa = pessoa,exposicao = exposicao)
        return ingresso   
    
    @staticmethod
    def excluiringresso(id):
        ingresso = Ingresso.objects.get(pk=id)
        ingresso.delete()
        print("deletado com sucesso")


