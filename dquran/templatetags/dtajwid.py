from django import template

register = template.Library()


@register.filter
def get_iqlab(self):
    return self.get_iqlab()
