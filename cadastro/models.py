from django.db import models

# Create your models here.

class Curso(models.Model):

    id_curso = models.BigAutoField(primary_key = True)

    nome = models.CharField(max_length=200,
                            null=False)
    valor = models.DecimalField(max_length=11,
                                max_digits=11,
                                decimal_places=2,
                                null=False)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    dataInicio = models.DateTimeField(null=False)
    dataTermino = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.curso.nome} - {self.dataInicio} - {self.dataTermino}"