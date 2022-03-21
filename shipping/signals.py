from user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from shipping.models import Shipping, SendSale

@receiver(post_save, sender=SendSale)
def announce_new_sendsale(sender, instance, created, **kwargs):
    print("procesando")
    if created:
        print("se creo un nuevo dato")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "event.alarm",
                       "event": "new_created",
                       "text": instance.pk})
