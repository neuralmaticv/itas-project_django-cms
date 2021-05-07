# Generated by Django 3.2 on 2021-05-07 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20210507_2348'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
