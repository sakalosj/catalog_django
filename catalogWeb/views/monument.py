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
from catalogWeb.helpers import add_tab_name
from ..forms import RestorerForm, RestorerRemoveForm, MonumentForm, ProjectForm, ResearchForm,  MaterialForm
from ..models import Restorer, Monument, Project, Research, Material, Monument2Project

TAB_NAME = 'monument'

def monument_list(request):
    monuments = Monument.objects.all()
    context = {
        'monument_list': monuments,
        'tab_name': TAB_NAME,
            }

    return render(request, 'catalogWeb/monument/monument_list.html', context)


def monument_create(request):
    monument_form = MonumentForm(request.POST or None, request.FILES or None)
    album_form = AlbumForm(request.POST or None, request.FILES or None)
    context = {
        'monument_form': monument_form,
        'album_form': album_form,
        'tab_name': TAB_NAME,
            }

    if monument_form.is_valid() and album_form.is_valid():
        monument_instance = monument_form.save()
        ''' in form cleaned data multiple files are not available,
         therefore files are processed via view function no in form'''
        album_process_form(request, monument_instance.album)
        return HttpResponseRedirect(reverse('monumentList'))

    return render(request, 'catalogWeb/monument/monument_form.html', context)


class MonumentDelete(DeleteView):
    model = Monument
    template_name = 'catalogWeb/monument/monument_confirm_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('monument_list')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)


def monument_detail(request, pk):
    monument = get_object_or_404(Monument, pk=pk)
    album_html = album_show(monument.album)
    context = {'monument': monument,
               'album_html': album_html,
               'tab_name': TAB_NAME,
               }
    return render(request, 'catalogWeb/monument/monument_detail.html', context)


def monument_update(request, pk):
    monument_instance = get_object_or_404(Monument, pk=pk)
    monument_form = MonumentForm(request.POST or None, request.FILES or None, instance=monument_instance)
    ImageFormSet = inlineformset_factory(Album, Image,  extra=0, form=ImageForm, widgets={'image': PictureWidget,})
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    context = {
        'monument_form': monument_form,
        'album_form': album_form,
        'tab_name': TAB_NAME,
              }

    if request.method == 'POST':
        album_formset = ImageFormSet(request.POST, request.FILES, instance=monument_instance.album)
        if monument_form.is_valid() and album_formset.is_valid() and album_form.is_valid():
            album_formset.save()
            album_process_form(request, monument_instance.album)
            monument_form.save()
            return HttpResponseRedirect(reverse('monumentList'))
        else:
            context['album_formset'] = album_formset
            return render(request, 'catalogWeb/monument/monument_form.html', context)

    album_formset = ImageFormSet(instance=monument_instance.album)
    context['album_formset'] = album_formset
    return render(request, 'catalogWeb/monument/monument_form.html', context)

