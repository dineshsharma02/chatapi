# Generated by Django 4.0.4 on 2022-05-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericfileupload',
            name='file_upload',
            field=models.FileField(upload_to='profile_pics'),
        ),
    ]
