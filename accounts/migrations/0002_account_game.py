# Generated by Django 2.1.7 on 2019-06-22 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='games.Game', verbose_name='Игра'),
        ),
    ]
