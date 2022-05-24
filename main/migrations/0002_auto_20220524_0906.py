# Generated by Django 3.1.7 on 2022-05-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(null=True),
        ),
    ]
