# Generated by Django 4.2.17 on 2024-12-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_exam_level_status_remove_homework_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ManyToManyField(related_name='lessons', to='store.courses'),
        ),
    ]
