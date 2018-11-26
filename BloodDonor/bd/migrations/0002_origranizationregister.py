# Generated by Django 2.0.7 on 2018-11-26 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrigranizationRegister',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email_id', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd.City')),
            ],
        ),
    ]