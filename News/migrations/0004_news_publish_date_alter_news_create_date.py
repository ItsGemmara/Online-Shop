# Generated by Django 4.0 on 2022-01-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_remove_news_date_news_create_date_news_is_allowed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='publish_date',
            field=models.DateField(default='2012-09-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
