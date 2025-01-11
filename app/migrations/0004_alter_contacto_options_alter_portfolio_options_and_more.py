# Generated by Django 4.2 on 2025-01-10 23:56

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_portfolio_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Portafolio', 'verbose_name_plural': 'Portafolios'},
        ),
        migrations.AddField(
            model_name='contacto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-01-01 00:00:00', help_text='Fecha y hora de creación del registro.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Fecha y hora de la última actualización.'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(help_text='Correo electrónico válido del contacto.', max_length=254),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(help_text='Mensaje enviado por el contacto.'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(help_text='Nombre del contacto (máximo 50 caracteres).', max_length=50),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.CharField(help_text='Número de teléfono del contacto (máximo 30 caracteres).', max_length=30, validators=[app.models.validar_telefono]),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='descripcion',
            field=models.CharField(help_text='Descripción del portafolio (máximo 100 caracteres).', max_length=100),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='nombre',
            field=models.CharField(help_text='Nombre del portafolio (máximo 50 caracteres).', max_length=50),
        ),
    ]