# Generated by Django 2.0.1 on 2018-01-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='category',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='name',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='release_date',
        ),
        migrations.AddField(
            model_name='serie',
            name='texto',
            field=models.CharField(default=' ', max_length=10000),
            preserve_default=False,
        ),
    ]
