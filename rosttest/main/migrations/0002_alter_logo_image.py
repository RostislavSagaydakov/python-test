# Generated by Django 5.1.1 on 2024-10-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(upload_to='brand-logo', verbose_name='Logo Image'),
        ),
    ]
