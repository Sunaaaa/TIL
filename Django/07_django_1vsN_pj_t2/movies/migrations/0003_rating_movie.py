# Generated by Django 2.2.6 on 2019-11-15 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20191115_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
            preserve_default=False,
        ),
    ]
