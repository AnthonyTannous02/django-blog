# Generated by Django 5.0.6 on 2024-05-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_project', '0003_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog_project.tag'),
        ),
    ]
