# Generated by Django 5.0.7 on 2024-07-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
