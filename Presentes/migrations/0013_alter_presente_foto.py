# Generated by Django 5.0.1 on 2024-01-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presentes', '0012_alter_presente_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='E:\\Escola\\Presentes/static/imgs'),
        ),
    ]
