# Generated by Django 5.1.2 on 2024-11-05 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_horario_ocupacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='ocupacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao'),
            preserve_default=False,
        ),
    ]
