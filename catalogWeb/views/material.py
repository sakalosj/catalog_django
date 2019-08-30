from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from catalogWeb.filters import MaterialFilter
from catalogWeb.forms import MaterialForm
from catalogWeb.tables import MaterialTable
from catalogWeb.views import UrlViewMixin
from ..models import Material


class MaterialListView(UrlViewMixin, SingleTableMixin, generic.ListView):
    model = Material
    table_class = MaterialTable
    # template_name = 'catalogWeb/material/material_list.html'
    template_name = 'catalogWeb/generic/base_list.html'
    paginate_by = 10


class MaterialFilterView(UrlViewMixin, SingleTableMixin, FilterView):
    model = Material
    table_class = MaterialTable
    filterset_class = MaterialFilter

    # template_name = 'catalogWeb/material/material_filter_list.html'
    template_name = 'catalogWeb/generic/base_filter.html'


class MaterialCreateView(UrlViewMixin, CreateView):
    model = Material
    # template_name = 'catalogWeb/material/material_form.html'
    template_name = 'catalogWeb/generic/base_form.html'
    # fields = 'first_name', 'last_name', 'description'  # , 'username'#'email'
    form_class = MaterialForm
    success_url = reverse_lazy('materialList')


class MaterialDeleteView(DeleteView):
    model = Material
    fields = '__all__'
    # template_name = 'catalogWeb/material/material_confirm_delete.html'
    template_name = 'catalogWeb/generic/base_confirm_delete.html'
    success_url = reverse_lazy('materialList')


class MaterialDetailView(UrlViewMixin, DetailView):
    model = Material
    template_name = 'catalogWeb/material/material_detail.html'


class MaterialUpdateView(UrlViewMixin, UpdateView):
    model = Material
    form_class = MaterialForm
    # template_name = 'catalogWeb/material/material_form.html'
    template_name = 'catalogWeb/generic/base_form.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.request.session['back_url'] = request.get_full_path()

    def get_success_url(self):
        url = reverse_lazy('materialDetail', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        return super().form_valid(form)

