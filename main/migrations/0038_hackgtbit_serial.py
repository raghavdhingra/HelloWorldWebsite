# Generated by Django 2.2.2 on 2019-11-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_hackgtbit'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackgtbit',
            name='serial',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
