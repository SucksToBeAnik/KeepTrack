# Generated by Django 4.1 on 2022-09-14 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('skill', '0009_alter_skill_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillobj',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
