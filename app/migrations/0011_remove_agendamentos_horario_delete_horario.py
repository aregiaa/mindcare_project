# Generated by Django 5.1.2 on 2024-10-27 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_horario_agendamentos_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamentos',
            name='horario',
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
    ]