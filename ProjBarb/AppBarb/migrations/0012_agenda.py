# Generated by Django 5.0.3 on 2024-04-03 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBarb', '0011_rename_id_cliente_agendamento_id_cliente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.DateTimeField(blank=True, default=True)),
                ('id_agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppBarb.agendamento')),
            ],
        ),
    ]
