# Generated by Django 5.0.6 on 2024-05-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_project', '0002_remove_tag_post_post_tags_alter_author_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, to='blog_project.tag'),
        ),
    ]
