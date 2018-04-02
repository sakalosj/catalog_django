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
from catalogWeb.helpers import add_tab_name
from ..forms import ResearchForm, Project
from ..models import Research

TAB_NAME = 'research'


class ResearchListView(generic.ListView):
    model = Research
    template_name = 'catalogWeb/research/research_list.html'
    paginate_by = 10

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


def research_create(request, project_id=None):
    research_form = ResearchForm(request.POST or None, request.FILES or None)
    album_form = AlbumForm(request.POST or None, request.FILES or None)
    context = {
            'research_form': research_form,
            'album_form': album_form,
            'tab_name': TAB_NAME,
            'redirect_to': request.GET.get('redirect_to')
            }

    if research_form.is_valid() and album_form.is_valid():
        research_instance = research_form.save()
        ''' in form cleaned data multiple files are not available,
         therefore files are processed via view function no in form'''
        album_process_form(request, research_instance.album)

        if project_id:
            Project.objects.get(pk=project_id).research_set.add(research_instance)
            if request.POST['redirect_to'] is not 'None':
                return HttpResponseRedirect(request.POST['redirect_to'])
        return HttpResponseRedirect(reverse('researchList'))
    return render(request, 'catalogWeb/research/research_form.html', context)


class ResearchDelete(DeleteView):
    model = Research
    template_name = 'catalogWeb/research/research_confirm_delete.html'
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


def research_detail(request, pk):
    research = get_object_or_404(Research, pk=pk)
    album_html = album_show(research.album)
    context = {
        'research': research,
        'album_html': album_html,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to') or request.POST.get('redirect_to') ,
    }
    return render(request, 'catalogWeb/research/research_detail.html', context)


class ResearchUpdate(UpdateView):
    model = Research
    form_class = ResearchForm
    success_url = reverse_lazy('researchList')

    @add_tab_name(TAB_NAME)
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


def research_update(request, pk):
    research_instance = get_object_or_404(Research, pk=pk)
    research_form = ResearchForm(request.POST or None, request.FILES or None, instance=research_instance)
    ImageFormSet = inlineformset_factory(Album, Image,  extra=0, form=ImageForm, widgets={'image': PictureWidget, })
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    context = {
        'research_form': research_form,
        'album_form': album_form,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to'),
    }

    if request.method == 'POST':
        album_formset = ImageFormSet(request.POST, request.FILES, instance=research_instance.album)
        if research_form.is_valid() and album_formset.is_valid() and album_form.is_valid():
            album_formset.save()
            album_process_form(request, research_instance.album)
            research_form.save()
            if request.POST['redirect_to'] is not 'None':
                return HttpResponseRedirect(request.POST['redirect_to'])
            return HttpResponseRedirect(reverse('researchDetail', kwargs={'pk': pk}))
        else:
            context['album_formset'] = album_formset
            return render(request, 'catalogWeb/research/research_form.html', context)

    album_formset = ImageFormSet(instance=research_instance.album)
    context['album_formset'] = album_formset
    return render(request, 'catalogWeb/research/research_form.html', context)

