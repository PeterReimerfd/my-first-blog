# Generated by Django 2.2.24 on 2021-09-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210929_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='dframe',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]