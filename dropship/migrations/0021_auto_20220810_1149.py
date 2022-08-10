# Generated by Django 2.2.4 on 2022-08-10 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0020_auto_20220810_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='labels',
            field=models.ManyToManyField(related_name='issues', to='dropship.Label'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='dropship.Sprint'),
        ),
    ]