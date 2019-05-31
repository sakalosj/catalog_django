
from django.conf.urls import url

from album import views

urlpatterns = [
    url(r'image2/list', views.Image2ListView.as_view(), name='image2List'),
    url(r'image2/add', views.image2_create, name='image2Create'),
    url(r'image2/detail/(?P<pk>[0-9]+)/$', views.image2_detail, name='image2Detail'),

    url(r'^list', views.AlbumListView.as_view(), name='albumList'),
    url(r'^add1', views.album_create_html, name='album_create_html'),
    url(r'^add2', views.album_create, name='albumCreate'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='albumDetail'),
    url(r'^edit1/(?P<pk>[0-9]+)/$', views.album_edit_html, name='album_edit1'),
    url(r'^update_cbv/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='albumUpdate'),
    url(r'^edit_cbv/(?P<pk>[0-9]+)/$', views.AlbumEdit.as_view(), name='albumEdit'),
    url(r'^edit2/(?P<pk>[0-9]+)/$', views.album_edit_html2, name='album_edit2'),
    url(r'^edita/(?P<pk>[0-9]+)/$', views.album_edit_ajax, name='album_edita'),

    url(r'image/list', views.ImageListView.as_view(), name='imageList'),
    url(r'image/add', views.image_create, name='imageCreate'),

    url(r'test/list', views.TestListView.as_view(), name='testList'),
    url(r'test/add', views.test_create, name='test_create'),
    url(r'test/detail/(?P<pk>[0-9]+)/$', views.test_detail, name='test_detail'),
    url(r'test/edit/(?P<pk>[0-9]+)/$', views.test_edit, name='test_edit'),

]

