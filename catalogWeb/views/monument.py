from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from catalogWeb.filters import MonumentFilter
from catalogWeb.forms import MonumentForm
from catalogWeb.models import Monument
from catalogWeb.tables import MonumentTable


class MonumentListView(SingleTableMixin, generic.ListView):
    model = Monument
    table_class = MonumentTable
    template_name = 'catalogWeb/monument/monument_list.html'
    paginate_by = 10



class MonumentFilterView(SingleTableMixin, FilterView):
    table_class = MonumentTable
    filterset_class = MonumentFilter

    template_name = 'catalogWeb/monument/monument_filter_list.html'



class MonumentCreate(CreateView):
    model = Monument
    template_name = 'catalogWeb/monument/monument_form.html'
    # fields = '__all__'
    # exclude = ['album']
    form_class = MonumentForm
    success_url = reverse_lazy('monumentList')

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)
    #
    # def __init__(self):
    #     super().__init__()


# def monument_create(request, pk=None):
#     # if not pk:
#     #     monument_instance = Monument()
#     #     monument_instance.save()
#     monument_form = MonumentForm(request.POST or None, request.FILES or None)
#
#     # monument_instance = get_object_or_404(Monument, pk=pk)
#     monument_form = MonumentForm(request.POST or None, request.FILES or None, instance=monument_instance)
#     album_id = monument_instance.album.id
#
#     template = 'catalogWeb/generic/generic_form.html'
#     context = {
#         'form': monument_form,
#         'album_id': album_id,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     if request.method == 'POST':
#         if monument_form.is_valid():
#             monument_form.save()
#             return HttpResponseRedirect(reverse('monumentDetail', kwargs={'pk': pk}))
#         else:
#             return render(request, template, context)
#
#     return render(request, template, context)


class MonumentDelete(DeleteView):
    model = Monument
    fields = '__all__'
    template_name = 'catalogWeb/monument/monument_confirm_delete.html'
    success_url = reverse_lazy('monumentList')

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


class MonumentDetail(DetailView):
    model = Monument
    template_name = 'catalogWeb/monument/monument_detail.html'

    # propertiesList = [field.name for field in Monument._meta.fields if field.name != "id"]

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


# def monument_detail(request, pk):
#     monument = get_object_or_404(Monument, pk=pk)
#     album_html = album_show(monument.album)
#     context = {
#         'monument': monument,
#         'album_html': album_html,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     return render(request, 'catalogWeb/monument/monument_detail.html', context)


class MonumentUpdate(UpdateView):
    model = Monument
    form_class = MonumentForm
    template_name = 'catalogWeb/monument/monument_form.html'


    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.request.session['back_url'] = request.get_full_path()

    def get_success_url(self):

        url = reverse_lazy('monumentDetail', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        return super().form_valid(form)

