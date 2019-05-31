from django import forms
from catalogWeb.models import Restorer


class RestorerForm(forms.ModelForm):
    class Meta:
        model = Restorer
        # exclude = ['restorer_id']
        exclude = ['album']



class RestorerRemoveForm(forms.Form):
    pk = forms.IntegerField()

