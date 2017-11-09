from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import ModelFormMixin, UpdateView

from .forms import RestorerForm, RestorerRemoveForm
from .models import Restorer, Monument, Project, ResearchRelation
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def index(request):
    return render(request, 'index.html',{'tableData': Restorer.objects.all()})

def index2(request):
    return render(request, 'index2.html',{'tableData': Restorer.objects.all()})

def restorerAdd(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RestorerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RestorerForm()

    return render(request, 'restorerAdd.html', {'form': form})

def restorerList(request):
    return render(request, 'restorerList.html', {'restorerList': Restorer.objects.all()})

def restorerRemove(request):
    if request.method == 'POST':
        form = RestorerRemoveForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['pk']
            Restorer.objects.filter(restorer_id=id).delete()
            return HttpResponseRedirect('/')

    else:
        form = RestorerRemoveForm(request.POST)
    return render(request, 'restorerRemove.html', {'form': form})

def getTable(request):
    return render(request, 'getTable.html', {'tableData': Restorer.objects.all()})

#@csrf_exempt
def getVariableValue(request):
    request.session["t"]="5"
    if request.method == 'POST':
        request.session[request.POST['variable']] = request.POST['value']
        data = eval(request.session['model']).objects.all()
        return HttpResponseRedirect("request.POST['variable']] request.POST['value']")
    return render(request, 'getTable.html', {'tableData': eval(request.session['model']).objects.all()})

######################################################################################
def index_new(request):
    """
    View function for home page of site.
    """
    # # Generate counts of some of the main objects
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # # Available copies of books
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index_new.html',
        context={},
    )

class RestorerListView(generic.ListView):
    model = Restorer
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



class MonumentListView(generic.ListView):
    model = Monument
    paginate_by = 4


class MonumentCreate(CreateView):
    model = Monument
    fields = '__all__'
    success_url = reverse_lazy('monumentList')

class MonumentDelete(DeleteView):
    model = Monument
    fields = '__all__'
    success_url = reverse_lazy('monumentList')

class MonumentDetail(DetailView):
    model = Monument

class MonumentUpdate(UpdateView):
    model = Monument
    fields = '__all__'
    success_url = reverse_lazy('monumentList')

class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 4


class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projectList')

class ProjectDelete(DeleteView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projectList')

class ProjectDetail(DetailView):
    model = Project

class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projectList')