from django.db import models

# ALG: Modelagem dos dados da aplicacao
class Empreendimento(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao')
    endereco = models.CharField('Endereco', max_length=200)
    status = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome

class Colaborador(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=15)

    def __str__(self):
        return self.nome