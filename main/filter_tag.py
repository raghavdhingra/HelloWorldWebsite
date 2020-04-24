from django import template

register = template.Library()

@register.filter(name='specs')
def specs(value):
    arr = value.split("|")
    if arr[0] == None or arr[0] == "":
        return "Volunteer"
    else:
        return arr[0]

@register.filter(name='lastname')
def lastname(value):
    if value is None:
        return ""
    else:
        return value

@register.filter(name='profile_pic')
def profile_pic(value):
    if value is None:
        return "/static/assets/person.jpg"
    else:
        return value
