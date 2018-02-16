from django.conf.urls import url, include
from django.urls import reverse

from . import views

urlpatterns = [
    url(r'^$', views.index_new, name='index_new'),

    url(r'restorer/list', views.RestorerListView.as_view(), name='restorerList'),
    url(r'restorer/add', views.RestorerCreate.as_view(), name='restorerCreate'),
    url(r'restorer/del/(?P<pk>[0-9]+)/$', views.RestorerDelete.as_view(), name='restorerDelete'),
    url(r'restorer/details/(?P<pk>[0-9]+)/$', views.RestorerDetail.as_view(), name='restorerDetail'),
    url(r'restorer/update/(?P<pk>[0-9]+)/$', views.RestorerUpdate.as_view(), name='restorerUpdate'),

    url(r'monument/list', views.monument_list, name='monumentList'),
    url(r'monument/add', views.monument_create, name='monumentCreate'),
    url(r'monument/del/(?P<pk>[0-9]+)/$', views.MonumentDelete.as_view(), name='monumentDelete'),
    url(r'monument/details/(?P<pk>[0-9]+)/$', views.monument_detail, name='monumentDetail'),
    url(r'monument/update/(?P<pk>[0-9]+)/$', views.monument_update, name='monumentUpdate'),

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
    url(r'material/add', views.material_create, name='materialCreate'),
    url(r'material/del/(?P<pk>[0-9]+)/$', views.MaterialDelete.as_view(), name='materialDelete'),
    url(r'material/details/(?P<pk>[0-9]+)/$', views.MaterialDetail.as_view(), name='materialDetail'),
    url(r'material/update/(?P<pk>[0-9]+)/$', views.MaterialUpdate.as_view(), name='materialUpdate'),

    url(r'album', include('album.urls')),
    # url(r'image/list', views.ImageListView.as_view(), name='imageList'),
    # url(r'image/add', views.image_create, name='imageCreate'),
    # url(r'imagelist/show', views.ImageListView.as_view(), name='imageList'),
    #
    # url(r'album/list', views.AlbumListView.as_view(), name='albumList'),
    # url(r'album/add', views.album_create, name='albumCreate'),
    # url(r'album/detail/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='albumDetail'),
    #

    # url(r'picture/del/(?P<pk>[0-9]+)/$', views.PictureDelete.as_view(), name='pictureDelete'),
    # url(r'picture/details/(?P<pk>[0-9]+)/$', views.PictureDetail.as_view(), name='pictureDetail'),
    # url(r'picture/update/(?P<pk>[0-9]+)/$', views.PictureUpdate.as_view(), name='pictureUpdate'),

]

