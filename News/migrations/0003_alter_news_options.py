# Generated by Django 4.0 on 2022-02-04 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
