from django.db import models

# Create your models here.
class Exposicao (models.Model):

    dataexposicao = models.DateField('Data Exposição', auto_now=False, auto_now_add=False)
    #acervo = models.ForeignKey(Acervo, on_delete=models.CASCADE)
    #espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)

    @staticmethod
    def cadastrarexposicao (dataexposicao,acervo,espaco):
        exposicao = Exposicao.objects.create(dataexposicao = dataexposicao,acervo = acervo, espaco = espaco)
        return exposicao
    
    @staticmethod
    def excluirexposicao (id):
        exposicao = Exposicao.objects.get(pk=id)
        exposicao.delete()
        print("deletado com sucesso")