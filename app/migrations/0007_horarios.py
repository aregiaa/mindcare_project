# Generated by Django 5.1.2 on 2024-10-27 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profissional')),
            ],
        ),
    ]
