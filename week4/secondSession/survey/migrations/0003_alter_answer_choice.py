# Generated by Django 3.2 on 2022-05-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_alter_answer_surveyidx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.TextField(),
        ),
    ]