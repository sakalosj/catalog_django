from django.conf.urls import url, include
from django.urls import reverse

from . import views

urlpatterns = [
    url(r'^$', views.index_new, name='index_new'),

    url(r'person/list', views.PersonListView.as_view(), name='personList'),
    url(r'person/filter', views.PersonFilterView.as_view(), name='personFilter'),
    url(r'person/add', views.PersonCreateView.as_view(), name='personCreate'),
    url(r'person/del/(?P<pk>[0-9]+)/$', views.PersonDeleteView.as_view(), name='personDelete'),
    url(r'person/details/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(), name='personDetail'),
    url(r'person/update/(?P<pk>[0-9]+)/$', views.PersonUpdateView.as_view(), name='personUpdate'),

    url(r'monument/list', views.MonumentListView.as_view(), name='monumentList'),
    url(r'monument/filter', views.MonumentFilterView.as_view(), name='monumentFilter'),
    url(r'monument/add', views.MonumentCreateView.as_view(), name='monumentCreate'),
    url(r'monument/del/(?P<pk>[0-9]+)/$', views.MonumentDeleteView.as_view(), name='monumentDelete'),
    url(r'monument/details/(?P<pk>[0-9]+)/$', views.MonumentDetailView.as_view(), name='monumentDetail'),
    url(r'monument/update/(?P<pk>[0-9]+)/$', views.MonumentUpdateView.as_view(), name='monumentUpdate'),

    url(r'project/list', views.ProjectListView.as_view(), name='projectList'),
    url(r'project/add', views.ProjectCreateView.as_view(), name='projectCreate'),
    url(r'project/del/(?P<pk>[0-9]+)/$', views.ProjectDeleteView.as_view(), name='projectDelete'),
    url(r'project/details/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='projectDetail'),
    url(r'project/update/(?P<pk>[0-9]+)/$', views.ProjectUpdateView.as_view(), name='projectUpdate'),
    url(r'project/filter', views.ProjectFilterView.as_view(), name='projectFilter'),

    url(r'research/list', views.ResearchListView.as_view(), name='researchList'),
    url(r'research/add/(?:(?P<project_id>[0-9]+)/)?$', views.ResearchCreateView.as_view(), name='researchCreate'),
    # url(r'research/add', views.research_create, name='researchCreate'),
    url(r'research/del/(?P<pk>[0-9]+)/$', views.ResearchDeleteView.as_view(), name='researchDelete'),
    url(r'research/details/(?P<pk>[0-9]+)/$', views.ResearchDetailView.as_view(), name='researchDetail'),
    url(r'research/update/(?P<pk>[0-9]+)/$', views.ResearchUpdateView.as_view(), name='researchUpdate'),
    url(r'research/filter', views.ResearchFilterView.as_view(), name='researchFilter'),

    url(r'material/list', views.MaterialListView.as_view(), name='materialList'),
    url(r'material/add', views.MaterialCreateView.as_view(), name='materialCreate'),
    url(r'material/del/(?P<pk>[0-9]+)/$', views.MaterialDeleteView.as_view(), name='materialDelete'),
    url(r'material/details/(?P<pk>[0-9]+)/$', views.MaterialDetailView.as_view(), name='materialDetail'),
    url(r'material/update/(?P<pk>[0-9]+)/$', views.MaterialUpdateView.as_view(), name='materialUpdate'),
    url(r'material/filter', views.MaterialFilterView.as_view(), name='materialFilter'),

    url(r'album/', include('album.urls')),

]

