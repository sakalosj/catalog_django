from django import forms
from django.forms import HiddenInput

from .models import Restorer, MaterialList, Material2MaterialList, Material


class RestorerForm(forms.ModelForm):
    class Meta:
        model = Restorer
        fields = '__all__'
        # exclude = ['restorer_id']

class RestorerRemoveForm(forms.Form):
    pk = forms.IntegerField()

class MaterialListForm(forms.ModelForm):
    """Form to Edit a Child and Specify the Ordering and Relation to Family"""

    # materialListId = forms.IntegerField(widget=HiddenInput)
    # description = forms.CharField()


    class Meta():
        model = MaterialList
        fields = '__all__'
        # exclude = ['materials', ]

    def save(self, commit=True):
        materialList = MaterialList.objects.create(name = self.cleaned_data.get('name'))  # Save the child so we have an ID for the m2m

        materials = [material for material in  self.cleaned_data.get('materials') ]
        for material in materials:
            membership = Material2MaterialList.objects.create(materialList = materialList, material = material, description = 'TEST' ).save()

        # matrials = Material.objects.get(slug=family_slug)
        # description = self.cleaned_data.get('order')
        # Material2MaterialList.objects.create(family=family, child=child, order=order)
        #
        return self.instance

