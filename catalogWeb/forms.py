from django import forms
from .models import Restorer


class RestorerForm(forms.ModelForm):
    class Meta:
        model = Restorer
        fields = '__all__'
        # exclude = ['restorer_id']

class RestorerRemoveForm(forms.Form):
    pk = forms.IntegerField()

