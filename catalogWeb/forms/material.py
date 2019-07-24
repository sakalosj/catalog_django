from django import forms
from django.forms import HiddenInput, SelectMultiple, MultipleHiddenInput

from album.widgets import AlbumWidget
from catalogWeb.models import  Material, Monument, SelectDateWidget2, Project, \
    Research, Monument2Project, Monument2Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = ['album']

    # pictures = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)


