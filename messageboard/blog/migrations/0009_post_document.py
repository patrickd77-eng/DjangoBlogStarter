# Generated by Django 2.2.5 on 2019-09-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190924_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
    ]
