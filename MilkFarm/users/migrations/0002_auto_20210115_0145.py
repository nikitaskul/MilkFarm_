# Generated by Django 3.1.5 on 2021-01-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, max_length=150, verbose_name='Company'),
        ),
    ]
