# Generated by Django 3.0.5 on 2020-06-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200624_0305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default='2020-06-24', verbose_name='comment date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='topics',
            field=models.ManyToManyField(to='main_app.Topic'),
        ),
    ]
