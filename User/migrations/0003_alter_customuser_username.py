# Generated by Django 3.2.6 on 2021-08-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20210830_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=40),
        ),
    ]
