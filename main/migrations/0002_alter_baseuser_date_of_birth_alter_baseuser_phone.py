# Generated by Django 5.0.6 on 2024-07-03 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
