# Generated by Django 2.2.4 on 2022-08-10 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0011_auto_20220810_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='dropship.Sprint'),
        ),
    ]
