# Generated by Django 4.1 on 2022-09-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='keeptrack/images/'),
        ),
    ]
