# Generated by Django 2.2.13 on 2020-09-05 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.TextField(default='Nigeria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='fav_color',
            field=models.CharField(default='Blue', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=30),
            preserve_default=False,
        ),
    ]
