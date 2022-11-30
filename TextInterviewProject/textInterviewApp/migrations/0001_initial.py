# Generated by Django 4.1.3 on 2022-11-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('question_content', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=4000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
