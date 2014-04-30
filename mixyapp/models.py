from django.db import models
from shortuuidfield import ShortUUIDField

class Mixy(models.Model):
	uuid = ShortUUIDField()
	

class Mix(models.Model):
	name = models.CharField(max_length=50)
	mixy = models.ForeignKey('Mixy')


class MixItem(models.Model):
	url = models.TextField()
	mix = models.ForeignKey('Mix')

class Deck(models.Model):
	mixy = models.ForeignKey('Mixy')

class DeckItem(models.Model):
	url = models.TextField()
	deck = models.ForeignKey('Deck')	
