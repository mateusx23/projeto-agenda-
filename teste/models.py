from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=14, null=False)
    email = models.EmailField()
    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    nome = models.CharField(max_length=200, null=False)
    carga_horaria = models.CharField(max_length=14, null=False)
    investimento = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    def __str__(self):
        return self.nome
