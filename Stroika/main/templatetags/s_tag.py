from django import template
from main.models import Product_categories

register = template.Library()


@register.simple_tag()
def get_categories():
    return Product_categories.objects.all()

