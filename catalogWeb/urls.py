from django.conf.urls import url
from django.urls import reverse

from . import views

urlpatterns = [
    url(r'^$', views.index_new, name='index_new'),
    url(r'restorer/list', views.RestorerListView.as_view(), name='restorerList'),
    url(r'restorer/add', views.RestorerCreate.as_view(), name='restorerAdd'),
    url(r'restorer/del/(?P<pk>[0-9]+)/$', views.RestorerDelete.as_view(), name='restorerDel'),

    url(r'object/list', views.ObjectListView.as_view(), name='objectList'),
    url(r'object/add', views.ObjectCreate.as_view(), name='objectAdd'),
    url(r'objectdel/(?P<pk>[0-9]+)/$', views.ObjectDelete, name='objectDel'),
    #
    # url(r'add/project', views.projectAdd),
    # url(r'list/project', views.projectList),
    # url(r'del/project', views.projectRemove),
    #
    # url(r'table', views.getTable),
    # url(r'ddd', views.getVariableValue),
    #url(r'^$', views.restorerList, name='index'),
]