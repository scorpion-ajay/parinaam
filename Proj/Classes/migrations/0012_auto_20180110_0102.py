# Generated by Django 2.0 on 2018-01-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0011_auto_20180107_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='batch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='discipline',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='exam_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]