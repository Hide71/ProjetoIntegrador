# Generated by Django 5.0.3 on 2024-03-29 11:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBarb', '0004_remove_plano_descrição'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('observações', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBarb.cliente')),
            ],
        ),
    ]
