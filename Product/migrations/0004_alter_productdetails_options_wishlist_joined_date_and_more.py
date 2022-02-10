# Generated by Django 4.0 on 2022-02-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_salesman_productcomment_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productdetails',
            options={'verbose_name': 'Product Detail', 'verbose_name_plural': 'Product Details'},
        ),
        migrations.AddField(
            model_name='wishlist',
            name='joined_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='wishlistdetail',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
