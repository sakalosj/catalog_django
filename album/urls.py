
from django.conf.urls import url

from album import views

urlpatterns = [
    url(r'list', views.AlbumListView.as_view(), name='albumList'),
    url(r'add', views.album_create, name='albumCreate'),
    url(r'detail/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='albumDetail'),
    url(r'edit/(?P<pk>[0-9]+)/$', views.album_edit, name='album_edit'),

    url(r'image/list', views.ImageListView.as_view(), name='imageList'),
    url(r'image/add', views.image_create, name='imageCreate'),

]

