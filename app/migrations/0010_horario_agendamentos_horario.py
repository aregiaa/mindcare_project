# Generated by Django 5.1.2 on 2024-10-27 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_agendamentos_horario_delete_horarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('data', models.DateField()),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profissional')),
            ],
        ),
        migrations.AddField(
            model_name='agendamentos',
            name='horario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.horario'),
        ),
    ]