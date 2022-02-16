# Generated by Django 4.0 on 2022-02-16 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('img', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.BigIntegerField(null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='Product/video')),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('rate', models.FloatField(default=0)),
                ('img', models.ImageField(null=True, upload_to='Product/image')),
                ('product_slug', models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('rate', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Product Detail',
                'verbose_name_plural': 'Product Details',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Product/image')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WishListDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('product', models.ManyToManyField(to='Product.Product')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.wishlist')),
            ],
        ),
    ]
