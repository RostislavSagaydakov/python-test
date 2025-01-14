# Generated by Django 5.1.1 on 2024-10-14 07:43

import filebrowser.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_menuitem_popup_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='favicon',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Фавиконка'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='logo',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Логотип'),
        ),
    ]
