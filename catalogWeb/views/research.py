from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from catalogWeb.helpers import add_tab_name
from ..forms import ResearchForm
from ..models import Research

TAB_NAME = 'research'


class ResearchListView(generic.ListView):
    model = Research
    template_name = 'catalogWeb/research/research_list.html'
    paginate_by = 4

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ResearchCreate(CreateView):
    model = Research
    form_class = ResearchForm
    success_url = reverse_lazy('researchList')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ResearchDelete(DeleteView):
    model = Research
    fields = '__all__'
    success_url = reverse_lazy('researchList')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ResearchDetail(DetailView):
    model = Research

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ResearchUpdate(UpdateView):
    model = Research
    form_class = ResearchForm
    success_url = reverse_lazy('researchList')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
