# Generated by Django 4.1.3 on 2022-11-20 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.priority'),
        ),
    ]
