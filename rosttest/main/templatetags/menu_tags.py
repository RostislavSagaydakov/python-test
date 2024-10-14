from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('main/base/menu.html')
def show_menu():
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {'menu_items': menu_items}