from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView

from album.forms import AlbumForm, ImageForm
from album.models import Album, Image
from album.views import album_process_form, album_show
from album.widgets import PictureWidget
from catalogWeb.forms import RestorerForm
from catalogWeb.helpers import add_tab_name
from ..models import Restorer

TAB_NAME = 'restorer'


class RestorerListView(generic.ListView):
    model = Restorer
    template_name = 'catalogWeb/restorer/restorer_list.html'
    paginate_by = 10

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class RestorerCreate(CreateView):
    model = Restorer
    template_name = 'catalogWeb/restorer/restorer_form.html'
    fields = '__all__'
    success_url = reverse_lazy('restorerList')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)





def restorer_create(request, pk=None):
    # if not pk:
    #     restorer_instance = Restorer()
    #     restorer_instance.save()
    restorer_form = RestorerForm(request.POST or None, request.FILES or None)

    # restorer_instance = get_object_or_404(Restorer, pk=pk)
    restorer_form = RestorerForm(request.POST or None, request.FILES or None, instance=restorer_instance)
    album_id = restorer_instance.album.id

    template = 'catalogWeb/generic/generic_form.html'
    context = {
        'form': restorer_form,
        'album_id': album_id,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to'),
    }

    if request.method == 'POST':
        if restorer_form.is_valid():
            restorer_form.save()
            return HttpResponseRedirect(reverse('restorerDetail', kwargs={'pk': pk}))
        else:
            return render(request, template, context)

    return render(request, template, context)


class RestorerDelete(DeleteView):
    model = Restorer
    fields = '__all__'
    template_name = 'catalogWeb/restorer/restorer_confirm_delete.html'
    success_url = reverse_lazy('restorerList')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class RestorerDetail(DetailView):
    model = Restorer
    propertiesList = [field.name for field in Restorer._meta.fields if field.name != "id"]

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


def restorer_detail(request, pk):
    restorer = get_object_or_404(Restorer, pk=pk)
    album_html = album_show(restorer.album)
    context = {
        'restorer': restorer,
        'album_html': album_html,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to'),
    }

    return render(request, 'catalogWeb/restorer/restorer_detail.html', context)


class RestorerUpdate(UpdateView):
    model = Restorer

    fields = '__all__'
    success_url = reverse_lazy('restorerList')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


def restorer_update(request, pk):
    restorer_instance = get_object_or_404(Restorer, pk=pk)
    restorer_form = RestorerForm(request.POST or None, request.FILES or None, instance=restorer_instance)
    album_id = restorer_instance.album.id

    template = 'catalogWeb/generic/generic_form.html'
    context = {
        'form': restorer_form,
        'album_id': album_id,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to'),
    }

    if request.method == 'POST':
        if restorer_form.is_valid():
            restorer_form.save()
            return HttpResponseRedirect(reverse('restorerDetail', kwargs={'pk': pk}))
        else:
            return render(request, template, context)

    return render(request, template, context)
