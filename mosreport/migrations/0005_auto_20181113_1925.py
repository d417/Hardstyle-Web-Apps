# Generated by Django 2.1.3 on 2018-11-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosreport', '0004_auto_20181113_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='yyyymm',
        ),
        migrations.AddField(
            model_name='item',
            name='mon',
            field=models.CharField(choices=[(1, '1月'), (2, '2月'), (3, '3月'), (4, '4月'), (5, '5月'), (6, '6月'), (7, '7月'), (8, '8月'), (9, '9月'), (10, '10月'), (11, '11月'), (12, '12月')], default=11, max_length=3, verbose_name='提出月'),
        ),
    ]
