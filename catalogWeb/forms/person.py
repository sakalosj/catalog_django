from django import forms

from catalogWeb.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

        # exclude = ['restorer_id']
        exclude = ['album', 'person2user']


class PersonRemoveForm(forms.Form):
    pk = forms.IntegerField()
