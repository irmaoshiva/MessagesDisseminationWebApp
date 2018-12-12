# Generated by Django 2.1.4 on 2018-12-12 14:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('longit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('build_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Buildings')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('ist_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('range_user', models.IntegerField()),
                ('lat', models.FloatField()),
                ('longit', models.FloatField()),
                ('build_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Buildings')),
            ],
        ),
    ]
