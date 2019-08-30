from django import forms
from django.forms import BaseFormSet, BaseModelFormSet, BaseInlineFormSet

from album.models import Image, Album
from album.widgets import ImageWidget


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

        widgets = {
            'image': ImageWidget,
        }




class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        # fields = '__all__'
        # exclude = ['pictureList']
        exclude = '__all__'

    images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)





