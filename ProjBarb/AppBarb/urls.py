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

    path('agendamento/', views.agendamento, name='agendamento'),

    path('agendamento_add/', views.agendamento_add, name='agendamento_add'),

    path('agendamento_edit/<int:agendamento_id>', views.agendamento_edit, name='agendamento_edit'),

    path('agendamento_delete/<int:agendamento_id>', views.agendamento_delete, name='agendamento_delete'),


]