from django import forms

from catalogWeb.models import CustomUser


class RestorerForm(forms.ModelForm):
    class Meta:
        model = CustomUser

        # exclude = ['restorer_id']
        exclude = ['album']



class RestorerRemoveForm(forms.Form):
    pk = forms.IntegerField()

