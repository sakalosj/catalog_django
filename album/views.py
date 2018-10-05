from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader, Context
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from album.forms import ImageForm, AlbumForm, Image2Form
from album.models import Image, Album
from album.widgets import PictureWidget


def image_create(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('imageList'))
    return render(request, 'album/image_form.html', {'form': form})


class ImageListView(generic.ListView):
    model = Image
    paginate_by = 10


def image2_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'album/single_image_tmpl.html', {'image': image})

def image2_create(request):
    form = Image2Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('image2List'))
    return render(request, 'album/image2_form.html', {'form': form})


class Image2ListView(generic.ListView):
    model = Image
    paginate_by = 10


def image_detail(request):
    pass


class AlbumDetailView(generic.DetailView):
    model = Album


class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 10


class AlbumCreate(generic.CreateView):
    model = Album
    fields = '__all__'
    paginate_by = 10
    success_url = reverse_lazy('albumList')


def album_create(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        files = request.FILES.getlist('pictures')
        for image in files:
            image = Image(image=image, album=instance)
            image.save()
        return HttpResponseRedirect(reverse('imageList'))

    return render(request, 'album/album_form.html', {'form': form})

def album_create(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        files = request.FILES.getlist('pictures')
        for image in files:
            image = Image(image=image, album=instance)
            image.save()
        return HttpResponseRedirect(reverse('imageList'))

    return render(request, 'album/album_form.html', {'form': form})


def album_process_form(request, album):
    form = AlbumForm(request.POST or None, request.FILES or None, instance=album)
    if form.is_valid():
        instance = form.save()
        files = request.FILES.getlist('pictures')
        for image in files:
            image = Image(image=image, album=instance)
            image.save()
        return instance
    return Album.objects.create()


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

# @csrf_exempt


def album_edit(request, pk):
    album_instance = get_object_or_404(Album, pk=pk)
    ImageFormSet = inlineformset_factory(Album, Image,  extra=0, form=ImageForm, widgets={'image': PictureWidget,})
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    if request.is_ajax():
        if request.POST['initial'] == 'True':
            album_formset = ImageFormSet(instance=album_instance)
            html = render(request, 'album/album_ajax_form.html',
                          {'album_formset': album_formset, 'album_form': album_form})
            t = loader.get_template('album/album_ajax_form.html')
            c = Context({'album_formset': album_formset, 'album_form': album_form})
            h = t.render({'album_formset': album_formset, 'album_form': album_form})
            return JsonResponse({'success': True, 'album_form': h})

        if request.POST['initial'] == 'False':
            album_formset = ImageFormSet(request.POST, request.FILES, instance=album_instance)
            if album_formset.is_valid() and album_form.is_valid():
                album_formset.save()
                album_process_form(request, album_instance)
                album_formset = ImageFormSet(instance=album_instance)
            html = render(request, 'album/album_ajax_form.html', {'album_formset': album_formset, 'album_form': album_form})
            t = loader.get_template('album/album_ajax_form.html')
            c = Context({'album_formset': album_formset, 'album_form': album_form})
            h = t.render({'album_formset': album_formset, 'album_form': album_form})
            return JsonResponse({'success': True, 'album_form': h})

    if request.method == 'GET':
        return render(request, 'album/album_form.html', {})

@csrf_exempt
def album_edit_html(request, pk):
    album_instance = get_object_or_404(Album, pk=pk)
    ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm )
    # ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': PictureWidget, })
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    if request.is_ajax():
        if request.POST['initial'] == 'True':
            album_formset = ImageFormSet(instance=album_instance)
            html = render(request, 'album/album_ajax_form.html',
                          {'album_formset': album_formset, 'album_form': album_form})
            t = loader.get_template('album/album_ajax_form.html')
            c = Context({'album_formset': album_formset, 'album_form': album_form})
            h = t.render({'album_formset': album_formset, 'album_form': album_form})
            return JsonResponse({'success': True, 'album_form': h})

        if request.POST['initial'] == 'False':
            album_formset = ImageFormSet(request.POST, request.FILES, instance=album_instance)
            if album_formset.is_valid() and album_form.is_valid():
                album_formset.save()
                album_process_form(request, album_instance)
                album_formset = ImageFormSet(instance=album_instance)
            html = render(request, 'album/album_ajax_form.html',
                          {'album_formset': album_formset, 'album_form': album_form})
            t = loader.get_template('album/album_ajax_form.html')
            c = Context({'album_formset': album_formset, 'album_form': album_form})
            h = t.render({'album_formset': album_formset, 'album_form': album_form})
            return JsonResponse({'success': True, 'album_form': h})

    else:
        t = loader.get_template('album/album_form2.html')
        c = Context({'album_form': album_form})
        h = t.render({'album_form': album_form})
        # return h
        #def render(request, template_name, context=None, content_type=None, status=None, using=None):
        return render(request,'album/album_form2.html',context={'album_form': album_form})

def album_edit_html_is_valid(request):
    ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': PictureWidget, })
    album_form = AlbumForm(request.POST or None, request.FILES or None)
    return album_form.is_valid()

    #
    # if request.method == 'POST':
    #     album_formset = ImageFormSet(request.POST, request.FILES, instance=album_instance)
    #     if album_formset.is_valid() and album_form.is_valid():
    #         album_formset.save()
    #         album_process_form(request, album_instance)
    #         return HttpResponseRedirect(reverse('monumentList'))
    #     else:
    #         return render(request, 'album/album_form.html', {'album_formset': album_formset, 'album_form': album_form})
    #
    # album_formset = ImageFormSet(instance=album_instance)
    # return render(request, 'album/album_form.html', {'album_formset': album_formset, 'album_form': album_form})



# def album_edit(album, image_dev_id="album", edit=False):
#     if image_dev_id is None:
#         image_dev_id = 'album_id_%s' % album.id
#     htmlDivContent = ['<div id = %s>' % image_dev_id]
#     for image in album.imageList.all():
#         htmlDivContent.append('<p> %s </p>' % image.name)
#         htmlDivContent.append('<figure>'
#                                 '<image src=%s><figcaption> %s </figcaption>'
#                               '</figure>' % (image.image.url, 'test'))
#     return '\n'.join(htmlDivContent)

