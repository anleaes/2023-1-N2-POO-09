from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    cpf = models.IntegerField('cpf', max_length=11)
    idade = models.IntegerField('Idade')
    dataNascimento = models.DateField('Data Nascimento', auto_now=False, auto_now_add=False)

    @staticmethod
    def cadastrarpessoa (nome,cpf,idade,datanascimento):
        pessoa = Pessoa.objects.create(nome = nome,cpf = cpf, idade = idade, datanascimento = datanascimento)
        return pessoa
    
    @staticmethod
    def consultarcpf(cpf):
        if len(cpf) == 11:
            return True
        return False
    
    @staticmethod
    def excluirpessoa (id):
        pessoa = Pessoa.objects.get(pk=id)
        pessoa.delete()
        print("deletado com sucesso")

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering =['id']

    #+cadastrarPessoa(nome, sobrenome, cpf, idade, dataNascimento)
    #+consultarCpf(cpf)
    #+excluirPessoa(id)