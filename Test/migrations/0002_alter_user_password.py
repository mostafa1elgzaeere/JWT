# Generated by Django 4.0.2 on 2022-07-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
