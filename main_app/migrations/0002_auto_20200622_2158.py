# Generated by Django 3.0.5 on 2020-06-22 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
