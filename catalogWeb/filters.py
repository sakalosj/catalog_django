from django import forms
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter

from catalogWeb.models import Person, Role


class PersonFilter(FilterSet):

    first_name = CharFilter(lookup_expr='contains',label='First')
    last_name = CharFilter(lookup_expr='iexact')
    roles = ModelMultipleChoiceFilter(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Person
        # fields = {'first_name': ['contains']}
        fields = []

class MonumentFilter(FilterSet):

    name = CharFilter(lookup_expr='contains',label='First')
    author = CharFilter(lookup_expr='iexact')
    # roles = ModelMultipleChoiceFilter(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Person
        # fields = {'first_name': ['contains']}
        fields = []
