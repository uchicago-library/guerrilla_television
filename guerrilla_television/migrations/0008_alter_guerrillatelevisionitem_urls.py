# Generated by Django 4.1.7 on 2023-03-23 18:34

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('guerrilla_television', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guerrillatelevisionitem',
            name='urls',
            field=modelcluster.fields.ParentalManyToManyField(to='guerrilla_television.url'),
        ),
    ]
