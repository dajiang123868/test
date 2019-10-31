# Generated by Django 2.2.6 on 2019-10-30 02:26

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('pub_time', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
