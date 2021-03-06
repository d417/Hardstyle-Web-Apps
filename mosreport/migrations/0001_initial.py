# Generated by Django 2.1.3 on 2018-11-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='氏名')),
                ('locale', models.CharField(max_length=200, verbose_name='顧客名/作業場所')),
                ('projectstatus', models.TextField(blank=True, max_length=300, verbose_name='案件状況')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
            ],
            options={
                'verbose_name': 'アイテム',
                'verbose_name_plural': 'アイテム',
            },
        ),
    ]
