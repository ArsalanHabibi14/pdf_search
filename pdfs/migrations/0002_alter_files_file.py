# Generated by Django 3.2.7 on 2022-06-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(max_length=2000, upload_to='files/'),
        ),
    ]
