# Generated by Django 4.0.3 on 2022-03-29 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_alter_note_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created']},
        ),
    ]
