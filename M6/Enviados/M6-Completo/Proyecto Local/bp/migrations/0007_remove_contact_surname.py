# Generated by Django 4.0.4 on 2022-05-12 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0006_alter_contact_cc_myself_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='surname',
        ),
    ]
