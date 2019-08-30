from django import forms
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter

from catalogWeb.models import Person, Role, Project, Research, Monument, Material


class PersonFilter(FilterSet):

    first_name = CharFilter(lookup_expr='contains',label='First')
    last_name = CharFilter(lookup_expr='iexact')
    roles = ModelMultipleChoiceFilter(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Person
        # fields = {'first_name': ['contains']}
        fields = []

class ProjectFilter(FilterSet):

    name = CharFilter(lookup_expr='contains',label='First')

    class Meta:
        model = Project
        # fields = {'first_name': ['contains']}
        fields = []

class MonumentFilter(FilterSet):

    name = CharFilter(lookup_expr='contains',label='First')
    author = CharFilter(lookup_expr='iexact')
    # roles = ModelMultipleChoiceFilter(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Monument
        # fields = {'first_name': ['contains']}
        fields = []

class ResearchFilter(FilterSet):

    name = CharFilter(lookup_expr='contains',label='First')
    # author = CharFilter(lookup_expr='iexact')
    # roles = ModelMultipleChoiceFilter(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Research
        # fields = {'first_name': ['contains']}
        fields = []


class MaterialFilter(FilterSet):

    name = CharFilter(lookup_expr='contains',label='First')
    # author = CharFilter(lookup_expr='iexact')
    # roles = ModelMultipleChoiceFilter(queryset=Role.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Material
        # fields = {'first_name': ['contains']}
        fields = []
