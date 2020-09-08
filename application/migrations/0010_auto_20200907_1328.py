# Generated by Django 2.2.13 on 2020-09-07 12:28

import application.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20200906_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='can_donate_for_bookdrive',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='idea_achieve_objectives',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='idea_funding',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='idea_project_successful',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='idea_promote_reading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=application.models.profile_image),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_approved',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_experienced_writer',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('M', 'Maybe')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='thoughts_on_writing_space',
            field=models.CharField(blank=True, choices=[('SA', 'Strongly Agree'), ('A', 'Agree'), ('N', 'Neutral'), ('D', 'Disagree'), ('SD', 'Strongly Disagree')], max_length=20, null=True),
        ),
    ]