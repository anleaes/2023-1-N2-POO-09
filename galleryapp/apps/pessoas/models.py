from django.db import models

# Create your models here.
class Pessoa ():
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    idade = models.IntegerField('Idade')
    dataNascimento = models.DateField('Data Nascimento', auto_now=False, auto_now_add=False)
    #+cadastrarPessoa(nome, sobrenome, cpf, idade, dataNascimento)
    #+consultarCpf(cpf)
    #+excluirPessoa(id)