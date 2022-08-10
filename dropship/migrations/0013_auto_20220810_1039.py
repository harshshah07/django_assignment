# Generated by Django 2.2.4 on 2022-08-10 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0012_auto_20220810_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='dropship.Sprint'),
        ),
        migrations.RemoveField(
            model_name='timelog',
            name='user',
        ),
        migrations.AddField(
            model_name='timelog',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='timelog', to=settings.AUTH_USER_MODEL),
        ),
    ]
