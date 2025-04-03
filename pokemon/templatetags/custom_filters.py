    
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def get_pokemon_id(url):
    try:
        return url.split('/')[-2]
    except IndexError:
        return ''

@register.filter(name='replace_hyphens')
def replace_hyphens(value):
    """Replaces hyphens with spaces in a string."""
    if isinstance(value, str):
        return mark_safe(value.replace('-', ' ')) # Use mark_safe if needed, good practice
    return value

# Add any other custom filters you might need here