# Generated by Django 4.0.4 on 2022-05-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0014_rename_order_id_orderdetail_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='presents',
            name='features',
            field=models.CharField(max_length=200, null=True),
        ),
    ]