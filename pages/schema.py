import graphene
from graphene_django import DjangoObjectType

from django.utils.translation import gettext_lazy as _

from .inputs import ItemInput
from .models import Item
from .types import ItemType


class LinkType(DjangoObjectType):
    class Meta:
        model = Item


class Query(graphene.ObjectType):
    items = graphene.List(ItemType)

    def resolve_items(self, info, **kwargs):
        return Item.objects.all()


class CreateItemMutation(graphene.Mutation):
    success = graphene.Boolean()
    item = graphene.String()
    ip = graphene.String()

    class Arguments:
        input = graphene.Argument(ItemInput)

    class Meta:
        description = _('Create an item for Agile Radar')

    @classmethod
    def mutate(cls, root, info, input):
        remote_host = info.context.META.get('REMOTE_HOST')
        remote_addr = info.context.META.get('REMOTE_ADDR')
        x_forwarded_for = info.context.META.get('HTTP_X_FORWARDED_FOR')
        ip = f"HOST: {remote_host}, ADDR: {remote_addr}, x_forwarded_for: {x_forwarded_for}"
        item = input.pop('item_text')

        return cls(success=True, ip=ip, item=item)


class Mutation(graphene.ObjectType):
    create_item = CreateItemMutation.Field()
