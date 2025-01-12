# Generated by Django 2.2.4 on 2022-08-10 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0010_auto_20220810_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('InProgress', 'InProgress'), ('InReview', 'InReview'), ('CodeComplete', 'CodeComplete'), ('QA Testing', 'QA Testing'), ('Done', 'Done')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='issue',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='dropship.Sprint'),
        ),
        migrations.CreateModel(
            name='watcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watcher', to='dropship.Issue')),
                ('watchers', models.ManyToManyField(null=True, related_name='issuedWatched', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timeSpent', models.CharField(max_length=10)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timelog', to='dropship.Issue')),
                ('user', models.ManyToManyField(related_name='timelog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dropship.Issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
