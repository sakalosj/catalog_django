from django import forms
from django.forms import HiddenInput, SelectMultiple, MultipleHiddenInput

from album.widgets import AlbumWidget
from .models import Restorer, Material, Monument, SelectDateWidget2, Project, \
    Research, Monument2Project, Monument2Material


class RestorerForm(forms.ModelForm):
    class Meta:
        model = Restorer
        fields = '__all__'
        # exclude = ['restorer_id']


class RestorerRemoveForm(forms.Form):
    pk = forms.IntegerField()


class MonumentForm(forms.ModelForm):
    class Meta:
        model = Monument
        exclude = ['materialList', 'album']
        # MaterialList = forms.ModelMultipleChoiceField(queryset=MaterialList.objects.filter(materials__material2materiallist__materialList_id__exact= 1))

    date = forms.DateField(widget=SelectDateWidget2)

    def save(self): #, album, commit=True):
        # self.instance.album = album
        self.instance.save()

        Monument2Material.objects.filter(monument=self.instance.id).delete()
        for material in self.cleaned_data.get('materials'):
            Monument2Material.objects.create(material=material, monument=self.instance, description='TEST')

        files = self.cleaned_data.get('pictures')


        # for file in files:
        #     image = Image(files)
        #     album.save()
        #     Image.objects.create(name=file, description=file, image=file, album=self.instance.album)

        return self.instance



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # exclude = ['monument_list']
        # widgets = {
        #     'monument_list': forms.HiddenInput(),
        # }

    monumentList = forms.ModelMultipleChoiceField(
        queryset=Monument.objects.all(),
        widget=MultipleHiddenInput
    )

    def save(self, commit=True):
        project = self.instance
        project.save()
        project.restorerList.set(self.cleaned_data['restorerList'])

        Monument2Project.objects.filter(project=self.instance.id).delete()
        for monument in self.cleaned_data['monumentList']:
            Monument2Project.objects.create(monument=monument, project=project)

        return self.instance


class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        exclude = ['monument', 'project', 'album']
        widgets = {
            'monument': forms.HiddenInput(),
            'project': forms.HiddenInput(),
        }

#
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['pictureList']
#
#
# class AlbumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'
#         # exclude = ['pictureList']
#
#     pictures = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = ['album']

    pictures = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)


