from django.db import models
from django.utils import timezone

from django import forms

# Create your models here.
class Plano(models.Model):
    plano = models.CharField(max_length=100)
    barba = models.IntegerField()
    corte = models.IntegerField()
    valor= models.DecimalField(max_digits=5, decimal_places=2) 

    def __str__(self):
        return self.plano


class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ('plano','barba', 'corte', 'valor')   

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereço = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    idPlano = models.ForeignKey(Plano, on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return self.nome

    

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome','endereço', 'telefone', 'cpf', 'idPlano')
       



class Agendamento(models.Model):
    METODO_PG_CHOICES = (
        ('pix', 'pix'), 
        ('cartao', 'cartao'), 
        ('dinheiro', 'dinheiro'),
        ('fiado', 'fiado')
    )
    STATUS_PG_CHOICES = (
        ('pg', 'Pago'),
        ('faltapg', 'Falta Pagamento'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=0)
    metodoPgto = models.CharField(max_length=100, null=True , choices= METODO_PG_CHOICES)
    statusPgto = models.CharField(max_length=10, null=True, choices= STATUS_PG_CHOICES)
    observacao = models.CharField(max_length=300, null=True )

    def __str__(self):
        return self.cliente.nome



class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ('cliente','data_hora', 'metodoPgto','statusPgto','observacao')