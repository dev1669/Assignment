# Generated by Django 3.1.2 on 2020-10-18 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20201018_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='cont_person_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_up', to='task.lead'),
        ),
    ]