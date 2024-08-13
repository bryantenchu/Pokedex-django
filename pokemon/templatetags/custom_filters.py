from django import template

register = template.Library()

@register.filter
def get_pokemon_id(url):
    try:
        return url.split('/')[-2]
    except IndexError:
        return ''