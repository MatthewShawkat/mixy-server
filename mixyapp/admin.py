from django.contrib import admin
from mixyapp.models import Mixy, Mix, Deck, MixItem, DeckItem
# Register your models here.
admin.site.register(Mixy)
admin.site.register(Mix)
admin.site.register(Deck)
admin.site.register(MixItem)
admin.site.register(DeckItem)
