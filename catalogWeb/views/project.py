import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import ModelFormMixin, UpdateView

from ..forms import ProjectForm, ResearchForm
from ..models import Monument, Project, Monument2Project

TAB_NAME = 'project'

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'catalogWeb/project/project_list.html'
    paginate_by = 10


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


# def project_create(request):
#     monuments = Monument.objects.all()
#     if request.method == 'POST':
#         project_form = ProjectForm(request.POST)
#         if project_form.is_valid():
#             project_form.save(json.loads(request.POST['monumentListJSON']))
#             return HttpResponseRedirect(reverse('projectList'))
#
#         else:
#             project_form = ProjectForm(request.POST)
#             researchForm = ResearchForm(request.POST)
#     else:
#         project_form = ProjectForm()
#         researchForm = ResearchForm()
#     return render(request, 'catalogWeb/project/project_form.html', {'project_form': project_form,'researchForm': researchForm, 'monuments': monuments})

def project_create(request, return_id=False):
    monuments = Monument.objects.all()
    project_form = ProjectForm(request.POST or None)
    context = {
        'project_form': project_form,
        'monuments': monuments,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to'),
    }

    if request.is_ajax():
        pass

    if project_form.is_valid():
        project = project_form.save()
        if return_id:
            return project.id
        return HttpResponseRedirect(reverse('projectList'))

    return render(request, 'catalogWeb/project/project_form.html', context)

# def monument_create(request):
#     monument_form = MonumentForm(request.POST or None, request.FILES or None)
#     album_form = AlbumForm(request.POST or None, request.FILES or None)
#     context = {
#         'monument_form': monument_form,
#         'album_form': album_form,
#         'tab_name': TAB_NAME,
#             }
#
#     if monument_form.is_valid() and album_form.is_valid():
#         monument_instance = monument_form.save()
#         ''' in form cleaned data multiple files are not available,
#          therefore files are processed via view function no in form'''
#         album_process_form(request, monument_instance.album)
#         return HttpResponseRedirect(reverse('monumentList'))
#
#     return render(request, 'catalogWeb/monument/monument_form.html', context)


class ProjectDelete(DeleteView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('projectList')


class ProjectDetail(DetailView):
    model = Project
    template_name = 'catalogWeb/project/project_detail.html'

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to'),
    }

    return render(request, 'catalogWeb/project/project_detail.html', context)


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


def project_update(request, pk):
    project_instance = get_object_or_404(Project, pk=pk)
    project_form = ProjectForm(request.POST or None, request.FILES or None, instance=project_instance)
    # ImageFormSet = inlineformset_factory(Album, Image,  extra=0, form=ImageForm, widgets={'image': PictureWidget, })
    # album_form = AlbumForm(request.POST or None, request.FILES or None)

    context = {
        'project_form': project_form,
        # 'album_form': album_form,
        'tab_name': TAB_NAME,
        'redirect_to': request.GET.get('redirect_to'),
    }

    if request.is_ajax():
        pass

    if request.method == 'POST':
        # album_formset = ImageFormSet(request.POST, request.FILES, instance=project_instance.album)
        if project_form.is_valid(): #and album_formset.is_valid() and album_form.is_valid():
            # album_formset.save()
            # album_process_form(request, project_instance.album)
            project_form.save()
            if request.is_ajax():
                return JsonResponse({'success': True})
            else:
                return HttpResponseRedirect(reverse('projectDetail', kwargs={'pk': pk}))

        else:
            # context['album_formset'] = album_formset
            if request.is_ajax():
                return JsonResponse({'error': True,
                                     'form': project_form.as_ul()})
            else:
                return render(request, 'catalogWeb/project/project_form.html', context)

    # album_formset = ImageFormSet(instance=project_instance.album)
    # context['album_formset'] = album_formset
    return render(request, 'catalogWeb/project/project_form.html', context)
