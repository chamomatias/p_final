# Generated by Django 4.2 on 2025-01-02 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contactos',
            new_name='contacto',
        ),
        migrations.RenameModel(
            old_name='Cursos',
            new_name='portfolio',
        ),
    ]