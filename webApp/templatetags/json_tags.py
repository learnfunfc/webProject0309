from django import template
import json

register = template.Library()

@register.filter
def json_to_list(value):
    list_string = ",".join(value)
    return json.loads(list_string)

@register.filter
def unicode_to_utf8(value):
    return str(value)
    

@register.filter
def json_to_list(value):
    josn_list = json.loads(value)
    return josn_list