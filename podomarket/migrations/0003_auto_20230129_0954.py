# Generated by Django 2.2 on 2023-01-29 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0002_auto_20230129_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='line_id',
            new_name='kakao_id',
        ),
    ]
