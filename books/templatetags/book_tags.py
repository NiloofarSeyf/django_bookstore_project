from django import template

register = template.Library()


# lowercase

@register.filter
def to_lowercase(value, args):
    return f'{args}:{value.lower()}'
    # return value.lower()
