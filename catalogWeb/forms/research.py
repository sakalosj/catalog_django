from django import forms
from django.forms import HiddenInput, SelectMultiple, MultipleHiddenInput

from album.widgets import AlbumWidget
from catalogWeb.models import  Material, Monument, SelectDateWidget2, Project, \
    Research, Monument2Project, Monument2Material


class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        exclude = ['monument', 'project', 'album']
        widgets = {
            'monument': forms.HiddenInput(),
            'project': forms.HiddenInput(),
        }
