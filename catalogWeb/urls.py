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
    url(r'monument/details/(?P<pk>[0-9]+)/$', views.MonumentDetail.as_view(), name='monumentDetail'),
    url(r'monument/update/(?P<pk>[0-9]+)/$', views.MonumentUpdate.as_view(), name='monumentUpdate'),

    url(r'project/list', views.ProjectListView.as_view(), name='projectList'),
    url(r'project/add', views.ProjectCreate.as_view(), name='projectCreate'),
    url(r'project/del/(?P<pk>[0-9]+)/$', views.ProjectDelete.as_view(), name='projectDelete'),
    url(r'project/details/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='projectDetail'),
    url(r'project/update/(?P<pk>[0-9]+)/$', views.ProjectUpdate.as_view(), name='projectUpdate'),

]