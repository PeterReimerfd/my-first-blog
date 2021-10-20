from django import template

register = template.Library()

@register.filter
def get_prop(obj, value):
    try:
        return obj[value]
    except:
        return obj