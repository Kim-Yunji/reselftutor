# Generated by Django 3.2.6 on 2021-09-08 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('tweet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweetmodel',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='tweetcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweetcomment',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.tweetmodel'),
        ),
    ]
