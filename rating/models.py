from django.db import models

from game import Player


class Rating(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    rating = models.IntegerField('Рейтинг', default=1000)

    class Meta:
        db_table = 'player_rating'
