# Generated by Django 4.2.7 on 2023-11-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blackcoffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.IntegerField(blank=True, max_length=5, null=True)),
                ('intensity', models.IntegerField(blank=True, max_length=5, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('insight', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=250, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('start_yaer', models.IntegerField(blank=True, max_length=5, null=True)),
                ('impact', models.IntegerField(blank=True, max_length=5, null=True)),
                ('added', models.DateTimeField(blank=True, null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('relevance', models.IntegerField(blank=True, max_length=5, null=True)),
                ('pestle', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('likelihood', models.IntegerField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
