# Generated by Django 3.1.1 on 2021-05-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210511_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom',
            name='quentity',
            field=models.CharField(default='1', max_length=200, null=True),
        ),
    ]
