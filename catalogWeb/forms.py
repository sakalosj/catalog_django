from django import forms
from django.forms import HiddenInput

from .models import Restorer, MaterialList, Material2MaterialList, Material, Monument, SelectDateWidget2


class RestorerForm(forms.ModelForm):
    class Meta:
        model = Restorer
        fields = '__all__'
        # exclude = ['restorer_id']


class RestorerRemoveForm(forms.Form):
    pk = forms.IntegerField()


class MaterialListForm(forms.ModelForm):
    class Meta():
        model = Monument
        fields = '__all__'

    def save(self, commit=True):
        materialList = MaterialList.objects.create(
            name=self.cleaned_data.get('name'))  # Save the child so we have an ID for the m2m
        materials = [material for material in self.cleaned_data.get('materials')]

        for material in materials:
            Material2MaterialList.objects.create(materialList=materialList, material=material,
                                                 description='TEST').save()

        return self.instance


class MonumentForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget2)

    def __init__(self, *args, **kwargs):
        super(MonumentForm, self).__init__(*args, **kwargs)
        # snip the other fields for the sake of brevity
        # Adding content to the form
        # queryset = MaterialList.objects.filter( id__exact = 1)
        # queryset = MaterialList.objects.get(id=1)
        # self.fields['materialList'] = forms.CharField()
        # for i in self.fields['materialList']:
        #     pass
        #     forms.ModelMultipleChoiceField(
        #     queryset=[MaterialList.objects.filter( id__exact = 1)]
        # )

    class Meta():
        model = Monument
        exclude = ['materialList']
        # MaterialList = forms.ModelMultipleChoiceField(queryset=MaterialList.objects.filter(materials__material2materiallist__materialList_id__exact= 1))

    test = forms.CharField(widget=forms.TextInput)

    # def save(self, commit=True):
    #     materialList = MaterialList.objects.create(name = self.cleaned_data.get('name'))  # Save the child so we have an ID for the m2m
    #     materials = [material for material in  self.cleaned_data.get('materials') ]
    #
    #     for material in materials:
    #         Material2MaterialList.objects.create(materialList = materialList, material = material, description = 'TEST' ).save()
    #
    #     return self.instance


class MaterialListForm2(forms.ModelForm):
    class Meta():
        model = MaterialList
        fields = '__all__'


    def save(self, commit=True):
        materialList = MaterialList.objects.update_or_create(id=self.instance.id)[0]  # Save the child so we have an ID for the m2m
        materials = [material for material in self.cleaned_data.get('materials')]
        Material2MaterialList.objects.filter(materialList = self.instance.id ).delete()

        for material in materials:
            Material2MaterialList.objects.create(materialList=materialList, material=material,description='TEST')
        return materialList

