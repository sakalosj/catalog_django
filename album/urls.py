
from django.conf.urls import url

from album import views

urlpatterns = [

    url(r'^list', views.AlbumListView.as_view(), name='albumList'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='albumDetail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.AlbumEdit.as_view(), name='albumEdit'),

]

