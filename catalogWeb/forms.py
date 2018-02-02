from django import forms
from django.forms import HiddenInput, SelectMultiple, MultipleHiddenInput

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
    date = forms.DateField(widget=SelectDateWidget2)

    class Meta():
        model = Monument
        exclude = ['materialList']
        # MaterialList = forms.ModelMultipleChoiceField(queryset=MaterialList.objects.filter(materials__material2materiallist__materialList_id__exact= 1))


    def save(self, commit=True):
        materials = [material for material in  self.cleaned_data.get('materials') ]
        self.instance.save()
        for material in self.cleaned_data.get('materials'):
            Monument2Material.objects.create(material = material, monument = self.instance, description = 'TEST' )

        return self.instance




class ProjectForm(forms.ModelForm):
    monumentList = forms.ModelMultipleChoiceField(
        queryset=Monument.objects.all(),
        widget=MultipleHiddenInput
    )
    class Meta():
        model = Project
        fields = '__all__'
        # exclude = ['monumentList']
        # widgets = {
        #     'monumentList': forms.HiddenInput(),
        # }

    def save(self, monumentList, commit=True):
        project = self.instance
        project.save()
        project.restorerList.set(self.cleaned_data['restorerList'])
        for monument in self.cleaned_data['monumentList']:
            Monument2Project.objects.create(monument=monument, project=project)
        return self.instance




class ResearchForm(forms.ModelForm):
    class Meta():
        model = Research
        exclude = ['monument','project']
        # fields = '__all__'
        widgets = {
            'monument': forms.HiddenInput(),
            'project': forms.HiddenInput(),
        }

