# Generated by Django 2.0.7 on 2019-07-30 19:45

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_teammember_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='contact',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={'address': '', 'email': '', 'phone': ''}),
        ),
        # migrations.AlterField(
        #     model_name='teammember',
        #     name='education',
        #     field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={'education': ['Education1', 'Education2']}),
        # ),
        migrations.AlterField(
            model_name='teammember',
            name='links',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={'facebook': 'https://www.facebook.com/', 'github': 'https://github.com/', 'twitter': 'https://twitter.com'}),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='skills',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={'skill': ['skill1', 'skill2']}),
        ),
    ]
