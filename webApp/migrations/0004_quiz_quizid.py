# Generated by Django 4.1.7 on 2023-03-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_quiz_question_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quizId',
            field=models.CharField(max_length=200, null=True),
        ),
    ]