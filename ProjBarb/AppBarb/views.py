from django.shortcuts import render, redirect
from AppBarb.models import Cliente,ClienteForm, Plano,PlanoForm, Contrato, ContratoForm, Agenda, AgendaForm

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

    return render(request, 'cliente/cliente_add.html', {'form': form })

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

   

def contrato(request):
    contratos = Contrato.objects.all()
    context = {
        'contratos': contratos
    }
    return render(request, 'contrato/contrato.html', context)


def contrato_add(request):
    form = ContratoForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contrato')
    context = {
        'form': form
         }
    return render(request, 'contrato/contrato_add.html', context)


def contrato_edit(request, contrato_id):
    contrato = Contrato.objects.get(id= contrato_id)
    form = ContratoForm(request.POST or None, instance= contrato)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contrato')
    context = {
        'form': form,
        'contrato': contrato

    }  
    return render(request, 'contrato/contrato_edit.html', context)  


def contrato_delete(request, contrato_id):
    contrato = Contrato.objects.get(id= contrato_id)
    contrato.delete()
    return redirect('contrato')



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


def agenda_edit(request, agenda_id):
    agenda = Agenda.objects.get(id= agenda_id)
    form = AgendaForm(request.POST or None, instance= agenda)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('agenda')
    context ={
        'form': form,
        'agenda': agenda
    }    
    return render(request, 'agenda/agenda_edit.html', context )


def agenda_delete(request, agenda_id):
    agenda = Agenda.objects.get(id= agenda_id)
    agenda.delete()
    return redirect('agenda')

