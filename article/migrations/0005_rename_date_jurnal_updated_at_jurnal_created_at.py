# Generated by Django 4.2.11 on 2024-03-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_band_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jurnal',
            old_name='date',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='jurnal',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]