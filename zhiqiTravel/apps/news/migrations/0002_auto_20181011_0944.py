# Generated by Django 2.1.2 on 2018-10-11 09:44

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '新闻信息', 'verbose_name_plural': '新闻信息'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]
