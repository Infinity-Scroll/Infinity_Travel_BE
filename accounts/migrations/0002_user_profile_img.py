# Generated by Django 5.0 on 2023-12-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='accounts/profile_img/%y/%m%d'),
        ),
    ]