import re
from collections import OrderedDict

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import Node, TemplateSyntaxError
from django.template.loader import get_template, select_template
from django.templatetags.l10n import register as l10n_register
from django.utils.html import escape
from django.utils.http import urlencode

import django_tables2 as tables
from django_tables2.utils import AttributeDict

register = template.Library()
kwarg_re = re.compile(r"(?:(.+)=)?(.+)")
context_processor_error_msg = (
    "Tag {%% %s %%} requires django.template.context_processors.request to be "
    "in the template configuration in "
    "settings.TEMPLATES[]OPTIONS.context_processors) in order for the included "
    "template tags to function correctly."
)
import datetime


@register.simple_tag
def ct(format_string):
    return datetime.datetime.now().strftime(format_string)


class RenderAlbumNode(Node):

    def __init__(self, album):
        super().__init__()
        self.album = album
        self.template_name = 'album/tag/album_detail_tag_template.html'

    def render(self, context):
        album = self.album.resolve(context)

        template = get_template(self.template_name)
        return template.render(context={'album': album})


@register.tag
def render_album(parser, token):
    bits = token.split_contents()
    bits.pop(0)  # tag_name

    album = parser.compile_filter(bits.pop(0))

    # tag_name, album, album_group = token.split_contents()

    return RenderAlbumNode(album)
