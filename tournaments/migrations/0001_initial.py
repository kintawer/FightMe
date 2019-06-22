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
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account', verbose_name='Аккаунт')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='ParticipantStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Статус участника турнира',
                'verbose_name_plural': 'Статусы участника турнира',
            },
        ),
        migrations.CreateModel(
            name='ParticipantStatusHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='Время')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tournaments.Participant', verbose_name='Участник')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.ParticipantStatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'История статуса',
                'verbose_name_plural': 'История статусов',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game', verbose_name='Игра')),
                ('participants', models.ManyToManyField(related_name='tournaments', through='tournaments.Participant', to='accounts.Account')),
            ],
            options={
                'verbose_name': 'Турнир',
                'verbose_name_plural': 'Турниры',
            },
        ),
        migrations.AddField(
            model_name='participant',
            name='status',
            field=models.ManyToManyField(through='tournaments.ParticipantStatusHistory', to='tournaments.ParticipantStatus'),
        ),
        migrations.AddField(
            model_name='participant',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='Турнир'),
        ),
    ]
