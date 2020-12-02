from django import template

register = template.Library()

@register.filter
def type_list_check(value):
    return isinstance(value, list)