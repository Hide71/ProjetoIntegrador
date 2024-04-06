from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
class Plano(models.Model):
    plano = models.CharField(max_length=100)
    barba = models.IntegerField()
    corte = models.IntegerField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)

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
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

    

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome','endereço', 'telefone', 'cpf')

   

class Contrato(models.Model):
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
    id_cliente = models.ForeignKey(Cliente,null=True, on_delete=models.CASCADE)
    id_plano = models.ForeignKey(Plano,null=True, on_delete=models.CASCADE)
    metodoPgto = models.CharField(max_length=100, null=True , choices= METODO_PG_CHOICES)
    statusPgto = models.CharField(max_length=10, null=True, choices= STATUS_PG_CHOICES)
    observacao = models.CharField(max_length=300, null=True )

    def __str__(self):
        return self.cliente



class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ('id_cliente', 'id_plano','metodoPgto','statusPgto','observacao')


class Agenda(models.Model):
    cliente = models.ForeignKey(Cliente,null=True, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano,null=True, on_delete=models.CASCADE)
    servico = models.DateTimeField(default=True, blank=True) 

    def __str__(self):
        return self.servico



class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('cliente', 'plano', 'servico',)