# Generated by Django 4.2 on 2025-01-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_contactos_contacto_rename_cursos_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
