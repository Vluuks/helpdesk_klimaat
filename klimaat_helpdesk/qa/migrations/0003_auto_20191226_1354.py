# Generated by Django 2.2.8 on 2019-12-26 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('qa', '0002_auto_20191226_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='answer')),
                ('date_submitted', models.DateTimeField(default=None, null=True, verbose_name='date answer submitted')),
                ('approved', models.BooleanField(default=False, verbose_name='answer approved')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_given', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='public',
            field=models.BooleanField(default=False, verbose_name='public'),
        ),
        migrations.AlterField(
            model_name='question',
            name='expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions_answered', to=settings.AUTH_USER_MODEL, verbose_name='Answered by'),
        ),
        migrations.AlterField(
            model_name='question',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Reviewd by'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(verbose_name='Reviewer remarks')),
                ('date_submission', models.DateTimeField(default=None, null=True, verbose_name='submission date')),
                ('approved', models.BooleanField(default=False)),
                ('approved_date', models.DateTimeField(default=None, null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='qa.Answer', verbose_name='review')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_reviews', to=settings.AUTH_USER_MODEL, verbose_name='reviewer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qa.Question', verbose_name='question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='system_tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]