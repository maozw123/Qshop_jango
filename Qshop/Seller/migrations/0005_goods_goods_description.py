# Generated by Django 2.1.8 on 2019-09-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0004_auto_20190910_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_description',
            field=models.TextField(default='好吃还不贵'),
        ),
    ]
