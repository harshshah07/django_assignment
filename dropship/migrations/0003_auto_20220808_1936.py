# Generated by Django 2.2.4 on 2022-08-08 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0002_auto_20220808_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectCreated', to=settings.AUTH_USER_MODEL),
        ),
    ]
