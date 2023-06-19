from django.db import models

# Create your models here.
class Espaco (models.Model):
    nome_espaco = models.CharField('Espaco', max_length=50)
    tipo_espaco = models.CharField('Tipo Espaço', max_length=50)
    lotacao = models.IntegerField('Lotação', max_length=3)

    @staticmethod
    def cadastrarEspaco (nome_espaco,tipo_espaco,lotacao):
        espaco = Espaco.objects.create(nome_espaco = nome_espaco, tipo_espaco = tipo_espaco, lotacao = lotacao)
        return espaco
    
    @staticmethod
    def excluirEspaco (id):
        espaco = Espaco.objects.get(pk=id)
        espaco.delete()
        print("deletado com sucesso")
