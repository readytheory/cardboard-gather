# Generated by Django 2.1.4 on 2019-01-06 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0003_auto_20190106_0227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rightanswer',
            old_name='right_answer',
            new_name='right_answer_text',
        ),
        migrations.RenameField(
            model_name='wronganswer',
            old_name='wrong_answer',
            new_name='wrong_answer_text',
        ),
    ]