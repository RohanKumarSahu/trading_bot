# Generated by Django 2.2.1 on 2021-03-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='direction',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='exchange',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='ticker',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
