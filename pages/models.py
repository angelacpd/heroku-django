from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    item_text = models.CharField(max_length=32)
    item_group = models.CharField(max_length=32)

    class Meta:
        app_label = 'pages'
        db_table = 'item'
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    def __str__(self):
        return f"{self.item.item_text}"

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)
