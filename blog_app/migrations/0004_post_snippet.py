# Generated by Django 3.2 on 2022-03-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link to Read Blog Post', max_length=200),
        ),
    ]
