# Generated by Django 3.2.7 on 2021-10-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_chapter_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='numeral',
            field=models.IntegerField(default=1),
        ),
    ]