# Generated by Django 5.1.1 on 2024-09-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
    ]
