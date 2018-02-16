from django import forms

from album.models import Image, Album
from album.widgets import PictureWidget


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pictureList']
        widgets = {
            'image': PictureWidget,
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        # exclude = ['pictureList']

    pictures = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)

class AlbumForm1(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        # exclude = ['pictureList']

    pictures = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))
