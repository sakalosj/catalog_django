import json

from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import ModelFormMixin, UpdateView

from album.forms import AlbumForm, ImageForm
from album.models import Album, Image
from album.views import album_show, album_process_form, album_edit_html_is_valid, album_edit_html
from album.widgets import PictureWidget
from ..forms import RestorerForm, RestorerRemoveForm, MonumentForm, ProjectForm, ResearchForm,  MaterialForm
from ..models import Restorer, Monument, Project, Research, Material, Monument2Project



class RestorerListView(generic.ListView):
    model = Restorer
    template_name = 'catalogWeb/restorer/restorer_list.html'
    paginate_by = 4


class RestorerCreate(CreateView):
    model = Restorer
    fields = '__all__'
    success_url = reverse_lazy('restorerList')

class RestorerDelete(DeleteView):
    model = Restorer
    fields = '__all__'
    success_url = reverse_lazy('restorerList')


class RestorerDetail(DetailView):
    model = Restorer
    propertiesList = [field.name for field in Restorer._meta.fields if field.name != "id"]

    def get_context_data(self, **kwargs):
        context = super(RestorerDetail, self).get_context_data(**kwargs)
        context['now'] = 'TERAZ'
        context['propertiesList'] = vars(self)
        return context


class RestorerUpdate(UpdateView):
    model = Restorer

    fields = '__all__'
    success_url = reverse_lazy('restorerList')
