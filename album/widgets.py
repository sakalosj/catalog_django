from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField, Widget


class PictureWidget(Widget):
    def render(self, name, value, attrs=None):
        html = Template('<img src="%s"/>' % value.url)
        return mark_safe(html.substitute(link=value))
