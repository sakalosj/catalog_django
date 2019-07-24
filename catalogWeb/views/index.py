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
from album.widgets import PictureWidget
# from .forms import RestorerForm, RestorerRemoveForm, MonumentForm, ProjectForm, ResearchForm,  MaterialForm
from ..models import  Monument, Project, Research, Material, Monument2Project



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
