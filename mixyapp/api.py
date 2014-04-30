from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from mixyapp.models import Mixy, Deck, DeckItem, Mix, MixItem

class MixItemResource(ModelResource):
    class Meta:
        queryset = MixItem.objects.all()
        resource_name = 'mixitem'
        list_allowed_methods = ['get', 'post']
        include_resource_uri = False
        authorization= Authorization()

class MixResource(ModelResource):
    class Meta:
        queryset = Mix.objects.all()
        resource_name = 'mix'
        list_allowed_methods = ['get', 'post']
        include_resource_uri = False
        authorization= Authorization()
    deckitems = fields.ToManyField(MixItemResource, 'mixitem_set', full=True, null=True)


class DeckItemResource(ModelResource):
    class Meta:
        queryset = DeckItem.objects.all()
        resource_name = 'deckitem'
        list_allowed_methods = ['get', 'post']
        include_resource_uri = False
        authorization= Authorization()

class DeckResource(ModelResource):
    class Meta:
        queryset = Deck.objects.all()
        resource_name = 'deck'
        list_allowed_methods = ['get', 'post']
        include_resource_uri = False
        authorization= Authorization()
    deckitems = fields.ToManyField(DeckItemResource, 'deckitem_set', full=True, null=True)

class MixyResource(ModelResource):
    class Meta:
        queryset = Mixy.objects.all()
        resource_name = 'mixy'
        list_allowed_methods = ['get', 'post', 'put']
        excludes = ['id']
        include_resource_uri = False
        authorization= Authorization()
        filtering = {
        	"uuid" : ['exact']
        }
    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])

        return data_dict
    decks = fields.ToManyField(DeckResource, 'deck_set' ,full=True, null=True)
    mixs = fields.ToManyField(DeckResource, 'mix_set' ,full=True, null=True)
