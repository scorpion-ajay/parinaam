# Generated by Django 2.0 on 2018-01-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=100)),
                ('discipline', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]