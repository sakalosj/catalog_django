from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import ModelFormMixin, UpdateView

from .forms import RestorerForm, RestorerRemoveForm, MaterialListForm, MonumentForm, MaterialListForm2
from .models import Restorer, Monument, Project, ResearchRelation, Research, Material, MaterialList, Monument2Project, \
    Material2MaterialList
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

#######################################################################

class MonumentListView(generic.ListView):
    model = Monument
    paginate_by = 4

def MonumentListViewF(request):
    monumentList = Monument.objects.all()
    context = {'monument_list' : monumentList}
    return render(request, 'catalogWeb/monument_list.html', context)


class MonumentCreate(CreateView):
    model = Monument
    fields = '__all__'
    success_url = reverse_lazy('monumentList')

def MonumentCreateF(request):
    #monumentList = Monument.objects.all()
    #context = {'monument_list' : monumentList}

    #materials = Material.objects.all()

    pass
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = MonumentForm(request.POST)
        form2 = MaterialListForm2(request.POST)

        # Check if the form is valid:
        if form.is_valid() and form2.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # monumentInst.due_back = form.cleaned_data['renewal_date']
            # monumentInst.save()
            monument = form.save(commit=False)
            monument.materialList = form2.save()
            monument.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('monumentList'))

    # If this is a GET (or any other method) create the default form.
    else:
        # proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        # form = MonumentForm(initial={'renewal_date': proposed_renewal_date, })
        form = MonumentForm()
        form2 = MaterialListForm2()

    return render(request, 'catalogWeb/monument_form.html', {'form': form, 'form2': form2})

class MonumentDelete(DeleteView):
    model = Monument
    fields = '__all__'
    success_url = reverse_lazy('monumentList')


class MonumentDetail(DetailView):
    model = Monument

def MonumentDetailF(request,pk):
    monument = get_object_or_404(Monument, pk=pk)
    materials = monument.materialList.materials.all()
    context = {'monument': monument,
               'materials': materials}

    return render(request, 'catalogWeb/monument_detail.html', context)


class MonumentUpdate(UpdateView):
    model = Monument
    form_class = MonumentForm
    # fields = '__all__'
    success_url = reverse_lazy('monumentList')

def MonumentUpdateF(request, pk):
    monumentInstance = get_object_or_404(Monument, pk=pk)
    # materialListInstance = get_object_or_404(MaterialList, pk=monumentInstance.materialList)
    form = MonumentForm(request.POST or None, instance=monumentInstance)
    form2 = MaterialListForm2(request.POST or None, instance=monumentInstance.materialList)
    #monumentList = Monument.objects.all()
    #context = {'monument_list' : monumentList}
    #materials = Material.objects.all()

    pass
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Check if the form is valid:
        if form.is_valid() and form2.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            # monumentInst.due_back = form.cleaned_data['renewal_date']
            # monumentInst.save()
            form.save()
            form2.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('monumentList'))

    # If this is a GET (or any other method) create the default form.
    else:
        # proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        # form = MonumentForm(initial={'renewal_date': proposed_renewal_date, })
        # form = MonumentForm(request.GET)
        # form2 = MaterialListForm2()
        pass


    return render(request, 'catalogWeb/monument_form.html', {'form': form, 'form2': form2})

#######################################################################


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 4


class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projectList')

    def form_valid(self, form):
        self.object = form.save(commit=False,)
        self.object.save()
        for monument in form.cleaned_data['monumentList']:
            monument2Project = Monument2Project()
            monument2Project.project = self.object
            monument2Project.monument = monument
            monument2Project.save()
        return super(ModelFormMixin, self).form_valid(form)


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

    def form_valid(self, form):
        self.object = form.save(commit=False,)
        self.object.save()
        self.object.restorerList.add()
        self.object.restorerList.set(form.cleaned_data['restorerList'])
        for monument in form.cleaned_data['monumentList']:
            m2p = Monument2Project()
            m2p.project = self.object
            m2p.monument = monument
            a = Monument2Project.objects.filter( monument = monument, project=self.object)
            m2p.save()
        return super(ModelFormMixin, self).form_valid(form)

#######################################################################


class ResearchListView(generic.ListView):
    model = Research
    paginate_by = 4


class ResearchCreate(CreateView):
    model = Research
    fields = '__all__'
    success_url = reverse_lazy('researchList')


class ResearchDelete(DeleteView):
    model = Research
    fields = '__all__'
    success_url = reverse_lazy('researchList')


class ResearchDetail(DetailView):
    model = Research


class ResearchUpdate(UpdateView):
    model = Research
    fields = '__all__'
    success_url = reverse_lazy('researchList')

#######################################################################


class MaterialView(generic.ListView):
    model = Material
    paginate_by = 4


class MaterialCreate(CreateView):
    model = Material
    fields = '__all__'
    success_url = reverse_lazy('materialList')


class MaterialDelete(DeleteView):
    model = Material
    fields = '__all__'
    success_url = reverse_lazy('materialList')


class MaterialDetail(DetailView):
    model = Material


class MaterialUpdate(UpdateView):
    model = Material
    fields = '__all__'
    success_url = reverse_lazy('materialList')

#######################################################################


class MaterialListCreate(generic.CreateView):
    model = MaterialList
    # form_class = MaterialListForm2
    fields = '__all__'
    paginate_by = 4
    success_url = reverse_lazy('materialListList')

    def form_valid(self, form):
        self.object = form.save(commit=False,)
        self.object.save()
        for materials in form.cleaned_data['materials']:
            m2ml = Material2MaterialList()
            m2ml.materialList = self.object
            m2ml.material = materials
            m2ml.save()
        return super(ModelFormMixin, self).form_valid(form)


class MaterialListView(generic.ListView):
    model = MaterialList
    paginate_by = 10


class MaterialListDelete(DeleteView):
    model = MaterialList
    fields = '__all__'
    success_url = reverse_lazy('materialListList')


class MaterialListDetail(DetailView):
    model = MaterialList


class MaterialListUpdate(UpdateView):
    model = MaterialList
    # form_class = MaterialListForm2
    fields = '__all__'
    success_url = reverse_lazy('materialListList')

    def form_valid(self, form):
        self.object = form.save(commit=False,)
        self.object.save()
        for materials in form.cleaned_data['materials']:
            m2ml = Material2MaterialList()
            m2ml.materialList = self.object
            m2ml.material = materials
            m2ml.save()
        return super(ModelFormMixin, self).form_valid(form)



