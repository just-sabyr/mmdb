# Generated by Django 5.0.2 on 2024-02-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='description_fr',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviedetails',
            name='title_fr',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
