# Generated by Django 2.1 on 2019-03-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190306_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stack',
            field=models.IntegerField(),
        ),
    ]
