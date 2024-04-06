from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),

    path('cliente/', views.cliente, name="cliente"),

    path('cliente_add/', views.cliente_add, name='cliente_add'),

    path('cliente_edit/<int:cliente_id>', views.cliente_edit, name='cliente_edit'),

    path('cliente_delete/<int:cliente_id>', views.cliente_delete, name='cliente_delete'),
    
    path('plano/', views.plano, name='plano'),

    path('plano_add/', views.plano_add, name='plano_add'),

    path('plano_edit/<int:plano_id>',views.plano_edit, name='plano_edit'),

    path('plano_delete/<int:plano_id>', views.plano_delete, name='plano_delete'),

    path('contrato/', views.contrato, name='contrato'),

    path('contrato_add/', views.contrato_add, name='contrato_add'),

    path('contrato_edit/<int:contrato_id>', views.contrato_edit, name='contrato_edit'),

    path('contrato_delete/<int:contrato_id>', views.contrato_delete, name='contrato_delete'),

    path('agenda/', views.agenda, name='agenda'),

    path('agenda_add/', views.agenda_add, name='agenda_add'),

    path('agenda_edit/<int:agenda_id>', views.agenda_edit, name='agenda_edit'),


]