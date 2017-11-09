from django.conf.urls import url
from django.urls import reverse

from . import views

urlpatterns = [
    url(r'^$', views.index_new, name='index_new'),

    url(r'restorer/list', views.RestorerListView.as_view(), name='restorerList'),
    url(r'restorer/add', views.RestorerCreate.as_view(), name='restorerCreate'),
    url(r'restorer/del/(?P<pk>[0-9]+)/$', views.RestorerDelete.as_view(), name='restorerDelete'),
    url(r'restorer/details/(?P<pk>[0-9]+)/$', views.RestorerDetail.as_view(), name='restorerDetail'),
    url(r'restorer/update/(?P<pk>[0-9]+)/$', views.RestorerUpdate.as_view(), name='restorerUpdate'),

    url(r'monument/list', views.MonumentListView.as_view(), name='monumentList'),
    url(r'monument/add', views.MonumentCreate.as_view(), name='monumentCreate'),
    url(r'monument/del/(?P<pk>[0-9]+)/$', views.MonumentDelete.as_view(), name='monumentDelete'),

    url(r'project/list', views.ProjectListView.as_view(), name='projectList'),
    url(r'project/add', views.ProjectCreate.as_view(), name='projectCreate'),
    url(r'project/del/(?P<pk>[0-9]+)/$', views.ProjectDelete.as_view(), name='projectDelete'),
    #
    # url(r'add/project', views.projectAdd),
    # url(r'list/project', views.projectList),
    # url(r'del/project', views.projectRemove),
    #
    # url(r'table', views.getTable),
    # url(r'ddd', views.getVariableValue),
    #url(r'^$', views.restorerList, name='index'),
]