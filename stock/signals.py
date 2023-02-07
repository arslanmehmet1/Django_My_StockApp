from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Purchases, Sales, Product


@receiver(pre_save, sender=Purchases)
def create_Token(sender, instance, **kwargs):
    product=Product.objects.get(id=instance.product_id)
    product["stock"]+=instance.quantity
    product.save()


# Product.objects.create(user=instance)
# @receiver(pre_save, sender=Sales)
# def calculate_total_price(sender, instance, **kwargs):
#     instance.price_total = instance.quantity * instance.price