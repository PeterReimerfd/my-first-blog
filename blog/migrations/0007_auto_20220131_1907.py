# Generated by Django 2.2.24 on 2022-02-01 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220125_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dframe',
            name='num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]