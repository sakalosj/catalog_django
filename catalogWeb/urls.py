from django.conf.urls import url
from django.urls import reverse

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_new, name='index_new'),
    url(r'restorer/list', views.RestorerListView.as_view(), name='restorerList'),
    url(r'restorer/add', views.RestorerCreate.as_view(), name='restorerAdd'),
    #url(r'restorer/del', views.RestorerDelete.as_view(), name='restorerDel'),
    url(r'restorer/del/(?P<pk>[0-9]+)/$', views.RestorerDelete.as_view(), name='restorerDel'),

    # url(r'add/object', views.objectAdd),
    # url(r'list/object', views.objectList),
    # url(r'del/object', views.objectRemove),
    #
    # url(r'add/project', views.projectAdd),
    # url(r'list/project', views.projectList),
    # url(r'del/project', views.projectRemove),
    #
    # url(r'table', views.getTable),
    # url(r'ddd', views.getVariableValue),
    #url(r'^$', views.restorerList, name='index'),
]