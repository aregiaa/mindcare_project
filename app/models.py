from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
    
class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    pais = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    instituicao = models.ForeignKey('Instituicao', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Paciente(Pessoa):
    pass

    def __str__(self):
        return self.nome

class Profissional(Pessoa):
    pass

    def __str__(self):
        return self.nome
    
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    
class Horario(models.Model):
    hora = models.TimeField()
    data = models.DateField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.profissional} - {self.data} - {self.hora}'
    
 
class Agendamentos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, null=True)
    observacoes = models.TextField()

    

    def __str__(self):
        return f'{self.paciente} - {self.profissional} - {self.horario}' 
    
