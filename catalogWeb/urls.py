from django.conf.urls import url, include
from django.urls import reverse

from . import views

urlpatterns = [
    url(r'^$', views.index_new, name='index_new'),

    url(r'restorer/list', views.RestorerListView.as_view(), name='restorerList'),
    # url(r'restorer/add', views.restorer_create, name='restorerCreate'),
    url(r'restorer/add', views.RestorerCreate.as_view(), name='restorerCreate'),
    url(r'restorer/del/(?P<pk>[0-9]+)/$', views.RestorerDelete.as_view(), name='restorerDelete'),
    url(r'restorer/details/(?P<pk>[0-9]+)/$', views.restorer_detail, name='restorerDetail'),
    url(r'restorer/update/(?P<pk>[0-9]+)/$', views.restorer_update, name='restorerUpdate'),

    url(r'monument/list', views.monument_list, name='monumentList'),
    url(r'monument/add', views.monument_create, name='monumentCreate'),
    url(r'monument/del/(?P<pk>[0-9]+)/$', views.MonumentDelete.as_view(), name='monumentDelete'),
    url(r'monument/details/(?P<pk>[0-9]+)/$', views.monument_detail, name='monumentDetail'),
    url(r'monument/update/(?P<pk>[0-9]+)/$', views.monument_update, name='monumentUpdate'),

    url(r'project/list', views.ProjectListView.as_view(), name='projectList'),
    url(r'project/add', views.project_create, name='projectCreate'),
    url(r'project/del/(?P<pk>[0-9]+)/$', views.ProjectDelete.as_view(), name='projectDelete'),
    url(r'project/details/(?P<pk>[0-9]+)/$', views.project_detail, name='projectDetail'),
    url(r'project/update/(?P<pk>[0-9]+)/$', views.project_update, name='projectUpdate'),

    url(r'research/list', views.ResearchListView.as_view(), name='researchList'),
    url(r'research/add/(?:(?P<project_id>[0-9]+)/)?$', views.research_create, name='researchCreate'),
    # url(r'research/add', views.research_create, name='researchCreate'),
    url(r'research/del/(?P<pk>[0-9]+)/$', views.ResearchDelete.as_view(), name='researchDelete'),
    url(r'research/details/(?P<pk>[0-9]+)/$', views.research_detail, name='researchDetail'),
    url(r'research/update/(?P<pk>[0-9]+)/$', views.research_update, name='researchUpdate'),

    url(r'material/list', views.MaterialView.as_view(), name='materialList'),
    url(r'material/add', views.material_create, name='materialCreate'),
    url(r'material/del/(?P<pk>[0-9]+)/$', views.MaterialDelete.as_view(), name='materialDelete'),
    url(r'material/details/(?P<pk>[0-9]+)/$', views.material_detail, name='materialDetail'),
    url(r'material/update/(?P<pk>[0-9]+)/$', views.material_update, name='materialUpdate'),

    url(r'album/', include('album.urls')),

]

