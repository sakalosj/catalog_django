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
from album.views import album_show, album_process_form
from album.widgets import PictureWidget
from catalogWeb.helpers import add_tab_name
from ..forms import MonumentForm,  MaterialForm
from ..models import Monument, Material



TAB_NAME = 'material'

class MaterialView(generic.ListView):
    model = Material
    template_name = 'catalogWeb/material/material_list.html'
    paginate_by = 4

    @add_tab_name('material')
    def get_context_data(self):
        return super().get_context_data()


class MaterialCreate(CreateView):
    model = Material
    form_class = MaterialForm
    success_url = reverse_lazy('materialList')

    @add_tab_name('material')
    def get_context_data(self,*args, **kwargs):
        return super().get_context_data(*args, **kwargs)


def material_create(request, pk = None):
    material_form = MaterialForm(request.POST or None, request.FILES or None)
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    if material_form.is_valid() and album_form.is_valid():
        material_instance = material_form.save()
        album_process_form(request, material_instance.album)
        return HttpResponseRedirect(reverse('materialList'))

    return render(request, 'catalogWeb/material/material_form.html', {'material_form': material_form, 'album_form': album_form})


class MaterialDelete(DeleteView):
    model = Material
    fields = '__all__'
    template_name = 'catalogWeb/material/material_confirm_delete.html'
    success_url = reverse_lazy('materialList')


class MaterialDetail(DetailView):
    model = Material


def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)
    album_html = album_show(material.album)
    context = {'material': material,
               'album_html': album_html,
               'tab_name': TAB_NAME,
               }
    return render(request, 'catalogWeb/material/material_detail.html', context)


class MaterialUpdate(UpdateView):
    model = Material
    fields = '__all__'
    success_url = reverse_lazy('materialList')


def material_update(request, pk):
    material_instance = get_object_or_404(Material, pk=pk)
    material_form = MaterialForm(request.POST or None, request.FILES or None, instance=material_instance)
    ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': PictureWidget, })
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        album_formset = ImageFormSet(request.POST, request.FILES, instance=material_instance.album)
        if material_form.is_valid() and album_formset.is_valid() and album_form.is_valid():
            album_formset.save()
            album_process_form(request, material_instance.album)
            material_form.save()
            return HttpResponseRedirect(reverse('materialList'))
        else:
            return render(request, 'catalogWeb/material/material_form.html',
                          {'material_form': material_form,
                           'album_formset': album_formset,
                           'album_form': album_form,
                           'tab_name': TAB_NAME,
                           })

    album_formset = ImageFormSet(instance=material_instance.album)
    return render(request, 'catalogWeb/material/material_form.html',
                  {'material_form': material_form, 'album_formset': album_formset, 'album_form': album_form,'tab_name': TAB_NAME,})

