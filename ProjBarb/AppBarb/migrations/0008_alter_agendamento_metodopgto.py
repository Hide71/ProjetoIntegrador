# Generated by Django 5.0.3 on 2024-03-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBarb', '0007_rename_observações_agendamento_observacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='metodoPgto',
            field=models.CharField(choices=[('1', 'pix'), ('2', 'cartão'), ('3', 'dinheiro'), ('4', 'fiado')], max_length=100, null=True),
        ),
    ]
