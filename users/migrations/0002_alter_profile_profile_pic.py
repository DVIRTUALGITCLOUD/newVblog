# Generated by Django 3.2.6 on 2022-08-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='pictures/default_profile_pic.png', upload_to='pictures'),
        ),
    ]
