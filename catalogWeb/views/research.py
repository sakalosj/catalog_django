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



class ResearchListView(generic.ListView):
    model = Research
    template_name = 'catalogWeb/research/research_list.html'
    paginate_by = 4


class ResearchCreate(CreateView):
    model = Research
    form_class = ResearchForm
    success_url = reverse_lazy('researchList')


class ResearchDelete(DeleteView):
    model = Research
    fields = '__all__'
    success_url = reverse_lazy('researchList')


class ResearchDetail(DetailView):
    model = Research


class ResearchUpdate(UpdateView):
    model = Research
    form_class = ResearchForm
    success_url = reverse_lazy('researchList')

