# Generated by Django 3.2.18 on 2023-03-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]