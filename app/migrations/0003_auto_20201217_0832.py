# Generated by Django 2.0 on 2020-12-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201212_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='pics',
            field=models.ImageField(default='abc.jpg', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='customer',
            name='pics',
            field=models.ImageField(default='abc.jpg', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='weblink',
            field=models.CharField(default='abc.com', max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='weblink',
            field=models.CharField(default='abc.com', max_length=250),
        ),
    ]
