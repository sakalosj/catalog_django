from django import forms

from catalogWeb.models import Person


class RestorerForm(forms.ModelForm):
    class Meta:
        model = Person

        # exclude = ['restorer_id']
        exclude = ['album']



class RestorerRemoveForm(forms.Form):
    pk = forms.IntegerField()

