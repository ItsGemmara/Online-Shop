# Generated by Django 4.0 on 2022-01-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_remove_product_category_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category'),
        ),
    ]