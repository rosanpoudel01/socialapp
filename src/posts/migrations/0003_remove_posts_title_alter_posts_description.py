# Generated by Django 4.1.7 on 2023-03-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='title',
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
    ]
