# Generated by Django 5.0.1 on 2024-01-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presentes', '0003_alter_presente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='E:\\Escola\\Presentes\\Presentes\\static/imgs'),
        ),
    ]
