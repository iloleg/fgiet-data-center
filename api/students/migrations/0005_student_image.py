# Generated by Django 2.2.3 on 2019-07-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
