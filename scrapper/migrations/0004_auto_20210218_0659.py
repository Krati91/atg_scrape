# Generated by Django 3.1.6 on 2021-02-18 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0003_auto_20210218_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrapper.group'),
        ),
    ]
