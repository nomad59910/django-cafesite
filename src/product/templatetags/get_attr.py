from django import template


register = template.Library()


@register.filter(name="get_attr")
def get_attr(queryset, item_key):
    return getattr(queryset, item_key)
