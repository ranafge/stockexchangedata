# Generated by Django 3.2 on 2021-05-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_ecosoft', '0003_auto_20210506_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapyitemmodel',
            name='change',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
