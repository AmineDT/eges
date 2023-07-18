from django import template
import base64

register = template.Library()

@register.filter
def base64encode(value):
    # Check if the value is an ImageFieldFile object
    if value and hasattr(value, 'read'):
        binary_data = value.read()
        return base64.b64encode(binary_data).decode('utf-8')
    else:
        return ''
