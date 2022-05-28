# Generated by Django 3.2.11 on 2022-05-26 19:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name_question', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('visible', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]