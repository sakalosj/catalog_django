from django import forms
from django.forms import HiddenInput, SelectMultiple, MultipleHiddenInput

from album.widgets import AlbumWidget
from catalogWeb.models import  Material, Monument, SelectDateWidget2, Project, \
    Research, Monument2Project, Monument2Material


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # exclude = ['monument_list']
        # widgets = {
        #     'monument_list': forms.HiddenInput(),
        # }

    # monumentList = forms.ModelMultipleChoiceField(
    #     queryset=Monument.objects.all(),
    #     widget=MultipleHiddenInput
    # )

    def save(self, commit=True):
        project = self.instance
        project.save()
        project.restorerList.set(self.cleaned_data['restorerList'])
        #project.monument_list.set(self.cleaned_data['monument_list'])
        Monument2Project.objects.filter(project=self.instance.id).delete()
        for monument in self.cleaned_data['monument_list']:
            Monument2Project.objects.create(monument=monument, project=project)

        return self.instance
