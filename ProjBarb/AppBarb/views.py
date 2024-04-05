from django.shortcuts import render, redirect
from AppBarb.models import Cliente,ClienteForm, Plano,PlanoForm, Agendamento, AgendamentoForm, Agenda, AgendaForm

# Create your views here.
def home(request):
    return render(request, 'cliente/home.html')


def cliente(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'cliente/cliente.html', context)


def cliente_add(request):
    form = ClienteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cliente')
    context ={
        'form': form
    }        

    return render(request, 'cliente/cliente_add.html', context)

def cliente_edit(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cliente')
        
    context ={
        'cliente':cliente,
        'form': form
    }    

    return render(request, 'cliente/cliente_edit.html',context)

def cliente_delete(request, cliente_id):
    cliente = Cliente.objects.get(id= cliente_id)
    cliente.delete() 
    return redirect('cliente')


def plano(request):
    planos = Plano.objects.all()
    context ={
        'planos': planos
    }
    return render(request, 'plano/plano.html', context)

def plano_add(request):
    form = PlanoForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('plano')
    context = {
        'form':form
    }    
    return render(request, 'plano/plano_add.html',context)


def plano_edit(request, plano_id):
    plano = Plano.objects.get(id=plano_id)
    form = PlanoForm(request.POST or None, instance=plano)
    
    if request.POST:
        if form.is_valid():
           form.save()
           return redirect('plano')
    context = {
        'plano': plano,
        'form': form
    }       

    return render(request, 'plano/plano_edit.html',context)


def plano_delete(request, plano_id):
    plano = Plano.objects.get(id=plano_id)
    plano.delete()
    return redirect('plano')

   

def agendamento(request):
    agendamentos = Agendamento.objects.all()
    context = {
        'agendamentos': agendamentos
    }
    return render(request, 'agendamento/agendamento.html', context)


def agendamento_add(request):
    form = AgendamentoForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('agendamento')
    context = {
        'form': form
         }
    return render(request, 'agendamento/agendamento_add.html', context)


def agendamento_edit(request, agendamento_id):
    agendamento = Agendamento.objects.get(id= agendamento_id)
    form = AgendamentoForm(request.POST or None, instance= agendamento)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('agendamento')
    context = {
        'form': form,
        'agendamento':agendamento

    }  
    return render(request, 'agendamento/agendamento_edit.html', context)  


def agendamento_delete(request, agendamento_id):
    agendamento = Agendamento.objects.get(id= agendamento_id)
    agendamento.delete()
    return redirect('agendamento')



def agenda(request):
    agendas = Agenda.objects.all()
    context = {
        'agendas': agendas
    }
    return render(request, 'agenda/agenda.html', context)


def agenda_add(request):
    form = AgendaForm(request.POST or None)
    if request.POST:
         if form.is_valid():
             form.save()
             return redirect('agenda')
         
    context = {
        'form':form
    }
    return render(request, 'agenda/agenda_add.html', context)

