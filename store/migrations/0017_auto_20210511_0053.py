# Generated by Django 3.1.1 on 2021-05-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210510_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custom',
            old_name='size',
            new_name='design_size',
        ),
        migrations.AddField(
            model_name='custom',
            name='tshirt_size',
            field=models.CharField(choices=[('S', 's'), ('M', 'm'), ('L', 'l'), ('XL', 'xl'), ('XXL', 'xxl')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='custom',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]