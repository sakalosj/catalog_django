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
from ..forms import RestorerForm, RestorerRemoveForm, MonumentForm, ProjectForm, ResearchForm,  MaterialForm
from ..models import Restorer, Monument, Project, Research, Material, Monument2Project


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'catalogWeb/project/project_list.html'
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
    return render(request, 'catalogWeb/project/project_form.html', {'projectForm': projectForm,'researchForm': researchForm, 'monuments': monuments})


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

