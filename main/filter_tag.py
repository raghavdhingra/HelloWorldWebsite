from django import template

register = template.Library()

@register.filter(name='specs')
def specs(value):
    arr = value.split("|")
    return arr[0]

@register.filter(name='lastname')
def lastname(value):
    if value is None:
        return ""
    else:
        return value
