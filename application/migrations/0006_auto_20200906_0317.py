# Generated by Django 2.2.13 on 2020-09-06 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20200906_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='deputy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deputy_team_lead', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_lead', to=settings.AUTH_USER_MODEL),
        ),
    ]
