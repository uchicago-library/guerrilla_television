# Generated by Django 4.1.7 on 2023-03-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guerrilla_television', '0008_alter_guerrillatelevisionitem_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guerrillatelevisionitem',
            name='status',
            field=models.CharField(blank=True, choices=[('publish', 'publish'), ('private', 'private')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='guerrillatelevisionitem',
            name='urls',
            field=models.ManyToManyField(to='guerrilla_television.url'),
        ),
    ]
