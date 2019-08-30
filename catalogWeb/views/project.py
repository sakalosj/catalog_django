from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from catalogWeb.filters import ProjectFilter
from catalogWeb.forms import ProjectForm
from catalogWeb.tables import ProjectTable
from catalogWeb.views import UrlViewMixin
from ..models import Project


class ProjectListView(UrlViewMixin, SingleTableMixin, generic.ListView):
    model = Project
    table_class = ProjectTable
    # template_name = 'catalogWeb/project/project_list.html'
    template_name = 'catalogWeb/generic/base_list.html'
    paginate_by = 10


class ProjectFilterView(UrlViewMixin, SingleTableMixin, FilterView):
    model = Project
    table_class = ProjectTable
    filterset_class = ProjectFilter

    # template_name = 'catalogWeb/project/project_filter_list.html'
    template_name = 'catalogWeb/generic/base_filter.html'


class ProjectCreateView(UrlViewMixin, CreateView):
    model = Project
    # template_name = 'catalogWeb/project/project_form.html'
    template_name = 'catalogWeb/generic/base_form.html'
    # fields = 'name', 'last_name', 'description'  # , 'username'#'email'
    form_class = ProjectForm
    success_url = reverse_lazy('projectList')


class ProjectDeleteView(DeleteView):
    model = Project
    fields = '__all__'
    template_name = 'catalogWeb/project/project_confirm_delete.html'
    success_url = reverse_lazy('projectList')


class ProjectDetailView(UrlViewMixin, DetailView):
    model = Project
    template_name = 'catalogWeb/project/project_detail.html'


class ProjectUpdateView(UrlViewMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'catalogWeb/generic/base_form.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.request.session['back_url'] = request.get_full_path()

    def get_success_url(self):
        url = reverse_lazy('projectDetail', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        return super().form_valid(form)

