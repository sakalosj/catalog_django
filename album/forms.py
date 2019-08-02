from django import forms
from django.forms import BaseFormSet, BaseModelFormSet, BaseInlineFormSet

from album.models import Image, Album
from album.widgets import PictureWidget


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        # exclude = ['pictureList']

        widgets = {
            # 'picture': PictureWidget,
            'image': PictureWidget,
            # 'test': forms.TextInput
        }




class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        # fields = '__all__'
        # exclude = ['pictureList']
        exclude = '__all__'

    images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)





