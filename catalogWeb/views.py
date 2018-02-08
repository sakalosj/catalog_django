import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import ModelFormMixin, UpdateView
from .forms import RestorerForm, RestorerRemoveForm, MonumentForm, ProjectForm, ResearchForm, ImageForm, MaterialForm, \
    AlbumForm
from .models import Restorer, Monument, Project, Research, Material, Monument2Project, Image, Album


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

def MonumentListViewF(request):
    monumentList = Monument.objects.all()
    context = {'monument_list' : monumentList}
    return render(request, 'catalogWeb/monument_list.html', context)


def MonumentCreateF(request):
    albumInstance = get_object_or_404(Album, id=id)
    form = MonumentForm(request.POST or None, request.FILES or None)
    form2 = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return HttpResponseRedirect(reverse('monumentList'))
    return render(request, 'catalogWeb/monument_form.html', {'form': form, 'form2': form2})





class MonumentDelete(DeleteView):
    model = Monument
    fields = '__all__'
    success_url = reverse_lazy('monumentList')

def MonumentDetailF(request,pk):
    monument = get_object_or_404(Monument, pk=pk)
    context = {'monument': monument}
    return render(request, 'catalogWeb/monument_detail.html', context)


def MonumentUpdateF(request, pk):
    monumentInstance = get_object_or_404(Monument, pk=pk)
    form = MonumentForm(request.POST or None, request.FILES or None, instance=monumentInstance)

    if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('monumentList'))

    return render(request, 'catalogWeb/monument_form.html', {'form': form})

#######################################################################


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 4


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
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

def ProjectCreateF(request):
    monuments = Monument.objects.all()
    if request.method == 'POST':
        projectForm = ProjectForm(request.POST)
        if projectForm.is_valid() :
            projectForm.save(json.loads(request.POST['monumentListJSON']))
            return HttpResponseRedirect(reverse('projectList'))

        else:
            projectForm = ProjectForm(request.POST)
            researchForm = ResearchForm(request.POST)
    else:
        projectForm = ProjectForm()
        researchForm = ResearchForm()
    return render(request, 'catalogWeb/project_form.html', {'projectForm': projectForm,'researchForm': researchForm, 'monuments': monuments})


class ProjectDelete(DeleteView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projectList')


class ProjectDetail(DetailView):
    model = Project


class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
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
            a = Monument2Project.objects.filter(monument=monument, project=self.object)
            m2p.save()
        return super(ModelFormMixin, self).form_valid(form)

#######################################################################


class ResearchListView(generic.ListView):
    model = Research
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

#######################################################################


class MaterialView(generic.ListView):
    model = Material
    paginate_by = 4


class MaterialCreate(CreateView):
    model = Material
    form_class = MaterialForm
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


###########################################33


def ImageCreateF(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('imageList'))
    return render(request, 'catalogWeb/image_form.html', {'form': form})


class ImageListView(generic.ListView):
    model = Image
    paginate_by = 10

def ImageDetailF(request):
    pass

class AlbumDetailView(generic.DetailView):
    model = Album

class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 10

class AlbumCreate(generic.CreateView):
    model = Album
    fields = '__all__'
    paginate_by = 10
    success_url = reverse_lazy('albumList')
