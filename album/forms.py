from django import forms

from album.fields import PictureFields
from album.models import Image, Album, Image2, Test
from album.widgets import PictureWidget, PictureWidget2


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pictureList']
        widgets = {
            'image': PictureWidget,
        }

# class Image2Form(forms.Form):
#     a = PictureFields()
class Image2Form(forms.ModelForm):
    # picture = PictureFields()
    class Meta:
        model = Image2
        fields = ['name']
        # widgets = {
        #     'picture': PictureWidget,
        #     'test': forms.TextInput
        # }

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


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

