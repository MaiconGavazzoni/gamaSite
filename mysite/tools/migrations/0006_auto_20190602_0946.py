# Generated by Django 2.2.1 on 2019-06-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20190602_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock_code',
            field=models.IntegerField(verbose_name='Código Interno'),
        ),
    ]