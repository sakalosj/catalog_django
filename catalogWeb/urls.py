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

    url(r'monument/list', views.MonumentListViewF, name='monumentList'),
    url(r'monument/add', views.MonumentCreateF, name='monumentCreate'),
    url(r'monument/del/(?P<pk>[0-9]+)/$', views.MonumentDelete.as_view(), name='monumentDelete'),
    url(r'monument/details/(?P<pk>[0-9]+)/$', views.MonumentDetailF, name='monumentDetail'),
    url(r'monument/update/(?P<pk>[0-9]+)/$', views.MonumentUpdateF, name='monumentUpdate'),

    url(r'project/list', views.ProjectListView.as_view(), name='projectList'),
    url(r'project/add', views.ProjectCreateF, name='projectCreate'),
    url(r'project/del/(?P<pk>[0-9]+)/$', views.ProjectDelete.as_view(), name='projectDelete'),
    url(r'project/details/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='projectDetail'),
    url(r'project/update/(?P<pk>[0-9]+)/$', views.ProjectUpdate.as_view(), name='projectUpdate'),

    url(r'research/list', views.ResearchListView.as_view(), name='researchList'),
    url(r'research/add', views.ResearchCreate.as_view(), name='researchCreate'),
    url(r'research/del/(?P<pk>[0-9]+)/$', views.ResearchDelete.as_view(), name='researchDelete'),
    url(r'research/details/(?P<pk>[0-9]+)/$', views.ResearchDetail.as_view(), name='researchDetail'),
    url(r'research/update/(?P<pk>[0-9]+)/$', views.ResearchUpdate.as_view(), name='researchUpdate'),

    url(r'material/list', views.MaterialView.as_view(), name='materialList'),
    url(r'material/add', views.MaterialCreate.as_view(), name='materialCreate'),
    url(r'material/del/(?P<pk>[0-9]+)/$', views.MaterialDelete.as_view(), name='materialDelete'),
    url(r'material/details/(?P<pk>[0-9]+)/$', views.MaterialDetail.as_view(), name='materialDetail'),
    url(r'material/update/(?P<pk>[0-9]+)/$', views.MaterialUpdate.as_view(), name='materialUpdate'),

    url(r'materialList/list', views.MaterialListView.as_view(), name='materialListList'),
    url(r'materialList/add', views.MaterialListCreate.as_view(), name='materialListCreate'),
    url(r'materialList/update/(?P<pk>[0-9]+)/$', views.MaterialListUpdate.as_view(), name='materialListUpdate'),
    url(r'materialList/del/(?P<pk>[0-9]+)/$', views.MaterialListDelete.as_view(), name='materialListDelete'),
    url(r'materialList/details/(?P<pk>[0-9]+)/$', views.MaterialListDetail.as_view(), name='materialListDetail'),

]
