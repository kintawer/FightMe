# Generated by Django 2.1.7 on 2019-06-22 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('tournaments', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(-1, 'Отменен'), (0, 'Ожидание'), (1, 'Завершен'), (2, 'Окончен в ничью')], default=0, verbose_name='Статус')),
                ('complete_time', models.DateTimeField(blank=True, null=True, verbose_name='Время окончания')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='simple_matches', to='games.Game', verbose_name='Игра')),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='los_matches', to='accounts.Account', verbose_name='Проигравший')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='win_matches', to='accounts.Account', verbose_name='Победитель')),
            ],
            options={
                'verbose_name': 'Обычный матч',
                'verbose_name_plural': 'Обычные матчи',
            },
        ),
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(-1, 'Отменен'), (0, 'Ожидание'), (1, 'Завершен'), (2, 'Окончен в ничью')], default=0, verbose_name='Статус')),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='accounts.Account', verbose_name='Проигравший')),
                ('tournament', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='Турнир')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='accounts.Account', verbose_name='Победитель')),
            ],
            options={
                'verbose_name': 'Турнирный матч',
                'verbose_name_plural': 'Турнирные матчи',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tournamentmatch',
            unique_together={('winner', 'loser')},
        ),
        migrations.AlterUniqueTogether(
            name='simplematch',
            unique_together={('winner', 'loser')},
        ),
    ]