# Generated by Django 4.1 on 2022-09-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0006_alter_skill_started_learning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='started_learning',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
