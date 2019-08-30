from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView

from album.forms import ImageForm
from album.models import Album, Image
from album.widgets import ImageWidget
from catalogWeb.filters import ResearchFilter
from catalogWeb.r_helpers import add_tab_name
from catalogWeb.tables import ResearchTable
from catalogWeb.views import UrlViewMixin, SingleTableMixin, FilterView
from ..forms import ResearchForm, Project
from ..models import Research

class ResearchListView(UrlViewMixin, SingleTableMixin, generic.ListView):
    model = Research
    table_class = ResearchTable
    # template_name = 'catalogWeb/research/research_list.html'
    template_name = 'catalogWeb/generic/base_list.html'
    paginate_by = 10



class ResearchFilterView(UrlViewMixin, SingleTableMixin, FilterView):
    model = Research
    table_class = ResearchTable
    filterset_class = ResearchFilter

    # template_name = 'catalogWeb/research/research_filter_list.html'
    template_name = 'catalogWeb/generic/base_filter.html'



class ResearchCreateView(UrlViewMixin, CreateView):
    model = Research
    # template_name = 'catalogWeb/research/research_form.html'
    template_name = 'catalogWeb/generic/base_form.html'
    # fields = 'name', 'description'  # , 'username'#'email'
    form_class = ResearchForm
    success_url = reverse_lazy('researchList')

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)
    #
    # def __init__(self):
    #     super().__init__()


# def research_create(request, pk=None):
#     # if not pk:
#     #     research_instance = Research()
#     #     research_instance.save()
#     research_form = ResearchForm(request.POST or None, request.FILES or None)
#
#     # research_instance = get_object_or_404(Research, pk=pk)
#     research_form = ResearchForm(request.POST or None, request.FILES or None, instance=research_instance)
#     album_id = research_instance.album.id
#
#     template = 'catalogWeb/generic/generic_form.html'
#     context = {
#         'form': research_form,
#         'album_id': album_id,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     if request.method == 'POST':
#         if research_form.is_valid():
#             research_form.save()
#             return HttpResponseRedirect(reverse('researchDetail', kwargs={'pk': pk}))
#         else:
#             return render(request, template, context)
#
#     return render(request, template, context)


class ResearchDeleteView(DeleteView):
    model = Research
    fields = '__all__'
    template_name = 'catalogWeb/research/research_confirm_delete.html'
    success_url = reverse_lazy('researchList')

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


class ResearchDetailView(UrlViewMixin, DetailView):
    model = Research
    template_name = 'catalogWeb/research/research_detail.html'

    # propertiesList = [field.name for field in Research._meta.fields if field.name != "id"]

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


# def research_detail(request, pk):
#     research = get_object_or_404(Research, pk=pk)
#     album_html = album_show(research.album)
#     context = {
#         'research': research,
#         'album_html': album_html,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     return render(request, 'catalogWeb/research/research_detail.html', context)


class ResearchUpdateView(UpdateView):
    model = Research
    form_class = ResearchForm
    template_name = 'catalogWeb/research/research_form.html'


    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.request.session['back_url'] = request.get_full_path()

    def get_success_url(self):

        url = reverse_lazy('researchDetail', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        return super().form_valid(form)




# TAB_NAME = 'research'


# class ResearchListView(generic.ListView):
#     model = Research
#     template_name = 'catalogWeb/research/research_list.html'
#     paginate_by = 10
#
#     @add_tab_name(TAB_NAME)
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#
#
# class ResearchCreate(CreateView):
#     model = Research
#     form_class = ResearchForm
#     success_url = reverse_lazy('researchList')
#
#     @add_tab_name(TAB_NAME)
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#
#
# def research_create(request, project_id=None):
#     research_form = ResearchForm(request.POST or None, request.FILES or None)
#     album_form = AlbumForm(request.POST or None, request.FILES or None)
#     context = {
#             'research_form': research_form,
#             'album_form': album_form,
#             'tab_name': TAB_NAME,
#             'redirect_to': request.GET.get('redirect_to')
#             }
#
#     if research_form.is_valid() and album_form.is_valid():
#         research_instance = research_form.save()
#         ''' in form cleaned data multiple files are not available,
#          therefore files are processed via view function no in form'''
#         album_process_form(request, research_instance.album)
#
#         if project_id:
#             Project.objects.get(pk=project_id).research_set.add(research_instance)
#             if request.POST['redirect_to'] is not 'None':
#                 return HttpResponseRedirect(request.POST['redirect_to'])
#         return HttpResponseRedirect(reverse('researchList'))
#     return render(request, 'catalogWeb/research/research_form.html', context)
#
#
# class ResearchDelete(DeleteView):
#     model = Research
#     template_name = 'catalogWeb/research/research_confirm_delete.html'
#     fields = '__all__'
#     success_url = reverse_lazy('researchList')
#
#     @add_tab_name(TAB_NAME)
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#
#
# class ResearchDetail(DetailView):
#     model = Research
#
#     @add_tab_name(TAB_NAME)
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#
#
# def research_detail(request, pk):
#     research = get_object_or_404(Research, pk=pk)
#     album_html = album_show(research.album)
#     context = {
#         'research': research,
#         'album_html': album_html,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to') or request.POST.get('redirect_to') ,
#     }
#     return render(request, 'catalogWeb/research/research_detail.html', context)
#
#
# class ResearchUpdate(UpdateView):
#     model = Research
#     form_class = ResearchForm
#     success_url = reverse_lazy('researchList')
#
#     @add_tab_name(TAB_NAME)
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#
#
# def research_update(request, pk):
#     research_instance = get_object_or_404(Research, pk=pk)
#     research_form = ResearchForm(request.POST or None, request.FILES or None, instance=research_instance)
#     ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': ImageWidget, })
#     album_form = AlbumForm(request.POST or None, request.FILES or None)
#
#     context = {
#         'research_form': research_form,
#         'album_form': album_form,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     if request.method == 'POST':
#         album_formset = ImageFormSet(request.POST, request.FILES, instance=research_instance.album)
#         if research_form.is_valid() and album_formset.is_valid() and album_form.is_valid():
#             album_formset.save()
#             album_process_form(request, research_instance.album)
#             research_form.save()
#             if request.POST['redirect_to'] is not 'None':
#                 return HttpResponseRedirect(request.POST['redirect_to'])
#             return HttpResponseRedirect(reverse('researchDetail', kwargs={'pk': pk}))
#         else:
#             context['album_formset'] = album_formset
#             return render(request, 'catalogWeb/research/research_form.html', context)
#
#     album_formset = ImageFormSet(instance=research_instance.album)
#     context['album_formset'] = album_formset
#     return render(request, 'catalogWeb/research/research_form.html', context)

