# Generated by Django 3.0.1 on 2020-01-04 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200105_0044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name': 'ModelName', 'verbose_name_plural': 'ModelNames'},
        ),
        migrations.AlterModelTable(
            name='article',
            table='Makale',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='Yorum',
        ),
    ]
