# Generated by Django 2.2.8 on 2019-12-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'User'), (2, 'Expert'), (3, 'Reviewer'), (4, 'Handler'), (5, 'Editor')], default=1, verbose_name='User Role'),
        ),
    ]
