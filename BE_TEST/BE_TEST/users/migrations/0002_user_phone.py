# Generated by Django 4.2.1 on 2023-06-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=2, max_length=11, verbose_name='전화번호'),
            preserve_default=False,
        ),
    ]
