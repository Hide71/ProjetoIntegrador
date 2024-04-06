# Generated by Django 5.0.3 on 2024-04-06 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBarb', '0016_delete_agenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.DateTimeField(blank=True, default=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppBarb.cliente')),
                ('plano', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppBarb.plano')),
            ],
        ),
    ]
