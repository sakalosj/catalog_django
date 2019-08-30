from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from catalogWeb.filters import PersonFilter
from catalogWeb.forms import PersonForm
from catalogWeb.tables import PersonTable
from catalogWeb.views import UrlViewMixin
from ..models import Person


class PersonListView(UrlViewMixin, SingleTableMixin, generic.ListView):
    model = Person
    table_class = PersonTable
    # template_name = 'catalogWeb/person/person_list.html'
    template_name = 'catalogWeb/generic/base_list.html'
    paginate_by = 10


class PersonFilterView(UrlViewMixin, SingleTableMixin, FilterView):
    model = Person
    table_class = PersonTable
    filterset_class = PersonFilter

    # template_name = 'catalogWeb/person/person_filter_list.html'
    template_name = 'catalogWeb/generic/base_filter.html'


class PersonCreateView(UrlViewMixin, CreateView):
    model = Person
    # template_name = 'catalogWeb/person/person_form.html'
    template_name = 'catalogWeb/generic/base_form.html'
    fields = 'first_name', 'last_name', 'description'  # , 'username'#'email'
    # form_class = PersonForm
    success_url = reverse_lazy('personList')


class PersonDeleteView(DeleteView):
    model = Person
    fields = '__all__'
    # template_name = 'catalogWeb/person/person_confirm_delete.html'
    template_name = 'catalogWeb/generic/base_confirm_delete.html'
    success_url = reverse_lazy('personList')


class PersonDetailView(UrlViewMixin, DetailView):
    model = Person
    template_name = 'catalogWeb/person/person_detail.html'


class PersonUpdateView(UrlViewMixin, UpdateView):
    model = Person
    form_class = PersonForm
    # template_name = 'catalogWeb/person/person_form.html'
    template_name = 'catalogWeb/generic/base_form.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.request.session['back_url'] = request.get_full_path()

    def get_success_url(self):
        url = reverse_lazy('personDetail', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        return super().form_valid(form)

