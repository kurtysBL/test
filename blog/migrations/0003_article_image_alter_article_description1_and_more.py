# Generated by Django 4.1.2 on 2022-10-31 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description1',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description2',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description3',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
