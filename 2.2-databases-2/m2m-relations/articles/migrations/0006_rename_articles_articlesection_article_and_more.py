# Generated by Django 4.0.2 on 2022-09-20 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_articlesection_options_alter_section_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlesection',
            old_name='articles',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='articlesection',
            old_name='sections',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='section_name',
            new_name='name',
        ),
    ]
