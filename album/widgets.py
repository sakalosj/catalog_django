from string import Template

from django.forms import MultiWidget, widgets
from django.utils.safestring import mark_safe
from django.forms import ImageField, Widget, Select


class PictureWidget(MultiWidget):

    def render(self, name, value, attrs=None):
        html = Template('<img src="%s"/>' % value.url)
        return mark_safe(html.substitute(link=value))


class PictureWidget2(MultiWidget):

    def __init__(self, attrs=None):
        _widgets = (
            widgets.TextInput(attrs=attrs),
            widgets.TextInput(attrs=attrs),
        )
        super().__init__(widgets=_widgets, attrs=attrs)


    def decompress(self, value):
        if value:
            return value.split("|")
        return ['', '']

class AlbumWidget(Select):
    pass
