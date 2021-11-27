# Generated by Django 3.2.9 on 2021-11-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadpdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='desc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
