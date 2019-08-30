from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView

from album.forms import ImageForm, AlbumForm
from album.models import Image, Album


class AlbumDetailView(generic.DetailView):
    model = Album

    def get(self, request, pk, *args, **kwargs):
        '''
        IS NECCESSSARY ????

        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''
        album = get_object_or_404(Album, pk=pk)
        return render(request, 'album/cbv/album_detail.html', {'album': album})


class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 10


def album_show(album, image_div_id="album", edit=False):
    if not album:  # if album is empty return None
        return None
    if image_div_id is None:
        image_div_id = 'album_id_%s' % album.id
    html_div_content = ['<div id = %s>' % image_div_id]
    for image in album.imageList.all():
        html_div_content.append('<p> %s </p>' % image.name)
        html_div_content.append('<figure>'
                                '<image src=%s><figcaption> %s </figcaption>'
                                '</figure>' % (image.image.url, 'test'))
    return '\n'.join(html_div_content)


class AlbumEdit(TemplateView):
    template_name = 'album/cbv/album_form.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.album_instance = get_object_or_404(Album, pk=self.kwargs['pk'])
        album_form = AlbumForm(request.POST or None, request.FILES or None, instance=self.album_instance)
        image_inlineformset_factory = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
        image_formset = image_inlineformset_factory(request.POST or None,
                                                    request.FILES or None,
                                                    instance=self.album_instance)

        self.forms = {'album_form': album_form,
                      'image_formset': image_formset}

        self.extra_context = self.forms


    def post(self, request, *args, **kwargs):

        if all([form.is_valid() for form in self.forms.values()]):
            self.forms['album_form'].save()
            self.forms['image_formset'].save()
            for image in request.FILES.getlist('images'):
                image = Image(image=image, album=self.album_instance)
                image.save()
        return HttpResponseRedirect(reverse('albumEdit', kwargs={'pk': self.kwargs['pk']}))

