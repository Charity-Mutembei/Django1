# Generated by Django 4.0 on 2022-05-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_image',
            field=models.ImageField(default='', upload_to='articles/'),
        ),
    ]