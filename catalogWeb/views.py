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
from .forms import RestorerForm, RestorerRemoveForm, MonumentForm, ProjectForm, ResearchForm,  MaterialForm
from .models import Restorer, Monument, Project, Research, Material, Monument2Project


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

def monument_list(request):
    monument_list = Monument.objects.all()
    context = {'monument_list': monument_list}
    return render(request, 'catalogWeb/monument_list.html', context)


def monument_create(request):
    monument_form = MonumentForm(request.POST or None, request.FILES or None)
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    if monument_form.is_valid() and album_form.is_valid():
        monument_instance = monument_form.save()
        ''' in form cleaned data multiple files are not available,
         therefore files are processed via view function no in form'''
        album_process_form(request, monument_instance.album)
        return HttpResponseRedirect(reverse('monumentList'))

    return render(request, 'catalogWeb/monument_form.html', {'monument_form': monument_form, 'album_form': album_form})


class MonumentDelete(DeleteView):
    model = Monument
    fields = '__all__'
    success_url = reverse_lazy('monument_list')


def monument_detail(request, pk):
    monument = get_object_or_404(Monument, pk=pk)
    album_html = album_show(monument.album)
    context = {'monument': monument,
               'album_html': album_html
               }
    return render(request, 'catalogWeb/monument_detail.html', context)


def monument_update(request, pk):
    monument_instance = get_object_or_404(Monument, pk=pk)
    monument_form = MonumentForm(request.POST or None, request.FILES or None, instance=monument_instance)
    ImageFormSet = inlineformset_factory(Album, Image,  extra=0, form=ImageForm, widgets={'image': PictureWidget,})
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        album_formset = ImageFormSet(request.POST, request.FILES, instance=monument_instance.album)
        if monument_form.is_valid() and album_formset.is_valid() and album_form.is_valid():
            album_formset.save()
            album_process_form(request, monument_instance.album)
            monument_form.save()
            return HttpResponseRedirect(reverse('monumentList'))
        else:
            return render(request, 'catalogWeb/monument_form.html', {'monument_form': monument_form, 'album_formset': album_formset, 'album_form': album_form})

    album_formset = ImageFormSet(instance=monument_instance.album)
    return render(request, 'catalogWeb/monument_form.html', {'monument_form': monument_form, 'album_formset': album_formset, 'album_form': album_form})

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
        if projectForm.is_valid():
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

def material_create(request,pk = None):
    material_form = MaterialForm(request.POST or None, request.FILES or None)
    aaa = Material.objects.filter(pk=pk)
    if not aaa.exists():
        album = Album.objects.create()
    album_form = AlbumForm(request.POST or None, request.FILES or None, instance=album)
    album_form = album_edit_html(request,album.id)

    if material_form.is_valid() :
        material_instance = material_form.save()
        # album_edit_html(request, material_form.id)
        return HttpResponseRedirect(reverse('monumentList'))

    return render(request, 'catalogWeb/material_form.html', {'material_form': material_form, 'album_form': album_form, 'album_id': album.id})

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


# def image_create(request):
#     form = ImageForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('imageList'))
#     return render(request, 'catalogWeb/image_form.html', {'form': form})
#
#
# class ImageListView(generic.ListView):
#     model = Image
#     paginate_by = 10
#
# def image_detail(request):
#     pass
#
# class AlbumDetailView(generic.DetailView):
#     model = Album
#
# class AlbumListView(generic.ListView):
#     model = Album
#     paginate_by = 10
#
# class AlbumCreate(generic.CreateView):
#     model = Album
#     fields = '__all__'
#     paginate_by = 10
#     success_url = reverse_lazy('albumList')
#
# def album_create(request):
#     form = AlbumForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save()
#         files = request.FILES.getlist('pictures')
#         for image in files:
#             image = Image(image=image, album=instance)
#             image.save()
#         return HttpResponseRedirect(reverse('imageList'))
#
#     return render(request, 'catalogWeb/album_form.html', {'form': form})
#
#
# def album_process_form(request):
#     form = AlbumForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save()
#         files = request.FILES.getlist('pictures')
#         for image in files:
#             image = Image(image=image, album=instance)
#             image.save()
#         return instance
#     return Album.objects.create()
#
# def album_show(album, imageDivID="album", edit=False):
#     if imageDivID is None:
#         imageDivID = 'album_id_%s' % album.id
#     htmlDivContent = ['<div id = %s>' % album]
#     for image in album.imageList.all():
#         htmlDivContent.append('<p> %s </p>' % image.name)
#         htmlDivContent.append('<figure>'
#                                 '<image src=%s><figcaption> %s </figcaption>'
#                               '</figure>' % (image.image.url, 'test'))
#     return '\n'.join(htmlDivContent)
