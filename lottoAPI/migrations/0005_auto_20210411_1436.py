# Generated by Django 3.2 on 2021-04-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottoAPI', '0004_auto_20210411_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gov_thai',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lao_lotto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lao_star',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lao_vip',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
