# Generated by Django 4.2.11 on 2024-03-30 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_jurnal_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('instrument', models.CharField(choices=[('g', 'Guiter'), ('b', 'Bass'), ('p', 'Pioner'), ('d', 'Dump')], max_length=1)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.band')),
            ],
        ),
    ]
