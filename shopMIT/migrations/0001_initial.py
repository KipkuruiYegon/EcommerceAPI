# Generated by Django 3.2.23 on 2023-11-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(default='product.jpg', upload_to='products')),
            ],
        ),
    ]