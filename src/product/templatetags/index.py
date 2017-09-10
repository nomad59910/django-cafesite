from django import template


register = template.Library()

@register.filter(name='index')
def index(l, i):
    try:
        return l[int(i)]
    except Exception as e:
        return None
