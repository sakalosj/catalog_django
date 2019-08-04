from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from catalogWeb.filters import PersonFilter
from catalogWeb.forms import PersonForm
from catalogWeb.tables import PersonTable
from ..models import Person



class PersonListView(SingleTableMixin, generic.ListView):
    model = Person
    table_class = PersonTable
    template_name = 'catalogWeb/person/person_list.html'
    paginate_by = 10



class PersonFilterView(SingleTableMixin, FilterView):
    table_class = PersonTable
    filterset_class = PersonFilter

    template_name = 'catalogWeb/person/person_filter_list.html'



class PersonCreate(CreateView):
    model = Person
    template_name = 'catalogWeb/person/person_form.html'
    fields = 'first_name', 'last_name', 'description'  # , 'username'#'email'
    # form_class = PersonForm
    success_url = reverse_lazy('personList')

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)
    #
    # def __init__(self):
    #     super().__init__()


# def person_create(request, pk=None):
#     # if not pk:
#     #     person_instance = Person()
#     #     person_instance.save()
#     person_form = PersonForm(request.POST or None, request.FILES or None)
#
#     # person_instance = get_object_or_404(Person, pk=pk)
#     person_form = PersonForm(request.POST or None, request.FILES or None, instance=person_instance)
#     album_id = person_instance.album.id
#
#     template = 'catalogWeb/generic/generic_form.html'
#     context = {
#         'form': person_form,
#         'album_id': album_id,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     if request.method == 'POST':
#         if person_form.is_valid():
#             person_form.save()
#             return HttpResponseRedirect(reverse('personDetail', kwargs={'pk': pk}))
#         else:
#             return render(request, template, context)
#
#     return render(request, template, context)


class PersonDelete(DeleteView):
    model = Person
    fields = '__all__'
    template_name = 'catalogWeb/person/person_confirm_delete.html'
    success_url = reverse_lazy('personList')

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


class PersonDetail(DetailView):
    model = Person
    template_name = 'catalogWeb/person/person_detail.html'

    # propertiesList = [field.name for field in Person._meta.fields if field.name != "id"]

    # @add_tab_name(TAB_NAME)
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)


# def person_detail(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     album_html = album_show(person.album)
#     context = {
#         'person': person,
#         'album_html': album_html,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     return render(request, 'catalogWeb/person/person_detail.html', context)


class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'catalogWeb/person/person_form.html'


    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.request.session['back_url'] = request.get_full_path()

    def get_success_url(self):

        url = reverse_lazy('personDetail', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        return super().form_valid(form)

# def person_update(request, pk):
#     person_instance = get_object_or_404(Person, pk=pk)
#     person_form = PersonForm(request.POST or None, request.FILES or None, instance=person_instance)
#     album_id = person_instance.album.id
#     album_form = person_instance.album
#
#     template = 'catalogWeb/generic/generic_form_html.html'
#     context = {
#         'form': person_form,
#         'album_id': album_id,
#         'tab_name': TAB_NAME,
#         'redirect_to': request.GET.get('redirect_to'),
#     }
#
#     if request.method == 'POST':
#         if person_form.is_valid():
#             person_form.save()
#             return HttpResponseRedirect(reverse('personDetail', kwargs={'pk': pk}))
#         else:
#             return render(request, template, context)
#
#     return render(request, template, context)
