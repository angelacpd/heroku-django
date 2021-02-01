from graphene_django import DjangoObjectType
from pages.models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item
