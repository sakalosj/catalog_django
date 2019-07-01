from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from album.forms import ImageForm, AlbumForm, Image2Form, TestForm
from album.models import Image, Album, Test
from album.widgets import PictureWidget


# def image_create(request):
#     form = ImageForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('imageList'))
#     return render(request, 'album/image_form.html', {'form': form})
#
#
# class ImageListView(generic.ListView):
#     model = Image
#     paginate_by = 10
#
#
# def image2_detail(request, pk):
#     image = get_object_or_404(Image, pk=pk)
#     return render(request, 'album/single_image_tmpl.html', {'image': image})
#
#
# def image2_create(request):
#     form = Image2Form(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('image2List'))
#     return render(request, 'album/image2_form.html', {'form': form})
#
#
# class Image2ListView(generic.ListView):
#     model = Image
#     paginate_by = 10


class AlbumDetailView(generic.DetailView):
    model = Album

    def get(self, request, pk, *args, **kwargs):
        album = get_object_or_404(Album, pk=pk)
        return render(request, 'album/album_detail.html', {'album': album})


class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 10


# class AlbumCreate(generic.CreateView):
#     model = Album
#     fields = '__all__'
#     paginate_by = 10
#     success_url = reverse_lazy('albumList')

#
# def album_create(request):
#     form = AlbumForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save()
#         files = request.FILES.getlist('pictures')
#         for image in files:
#             image = Image(image=image, album=instance)
#             image.save()
#         return HttpResponseRedirect(reverse('imageList'))
#
#     return render(request, 'album/album_form.html', {'form': form})
#
#
# def album_create_html(request):
#     form = AlbumForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         album_instance = form.save()
#         files = request.FILES.getlist('pictures')
#         for image in files:
#             image = Image(image=image, album=album_instance)
#             image.save()
#         return HttpResponseRedirect(reverse('album_edit1', args=[album_instance.pk]))
#
#     return render(request, 'album/album_form_html.html', {'album_form': form})
#
#
# def album_process_form(request, album):
#     form = AlbumForm(request.POST or None, request.FILES or None, instance=album)
#     if form.is_valid():
#         instance = form.save()
#         files = request.FILES.getlist('pictures')
#         for image in files:
#             image = Image(image=image, album=instance)
#             image.save()
#         return instance
#     return Album.objects.create()
#
#
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


# # @csrf_exempt
#
#
# def album_edit(request, pk):
#     album_instance = get_object_or_404(Album, pk=pk)
#     ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': PictureWidget, })
#     album_form = AlbumForm(request.POST or None, request.FILES or None)
#
#     if request.is_ajax():
#         if request.POST['initial'] == 'True':
#             album_formset = ImageFormSet(instance=album_instance)
#             html = render(request, 'album/album_ajax_form.html',
#                           {'album_formset': album_formset, 'album_form': album_form})
#             t = loader.get_template('album/album_ajax_form.html')
#             c = Context({'album_formset': album_formset, 'album_form': album_form})
#             h = t.render({'album_formset': album_formset, 'album_form': album_form})
#             return JsonResponse({'success': True, 'album_form': h})
#
#         if request.POST['initial'] == 'False':
#             album_formset = ImageFormSet(request.POST, request.FILES, instance=album_instance)
#             if album_formset.is_valid() and album_form.is_valid():
#                 album_formset.save()
#                 album_process_form(request, album_instance)
#                 album_formset = ImageFormSet(instance=album_instance)
#             html = render(request, 'album/album_ajax_form.html',
#                           {'album_formset': album_formset, 'album_form': album_form})
#             t = loader.get_template('album/album_ajax_form.html')
#             c = Context({'album_formset': album_formset, 'album_form': album_form})
#             h = t.render({'album_formset': album_formset, 'album_form': album_form})
#             return JsonResponse({'success': True, 'album_form': h})
#
#     if request.method == 'GET':
#         return render(request, 'album/album_form.html', {})
#
#
# class AlbumUpdate(generic.UpdateView):
#     template_name = 'album/cbv/album_form_html.html'
#     model = Album
#     # fields = '__all__'
#     form_class = AlbumForm
#     # success_url = reverse('albumEdit', args=[str(self.id)])
#
#     def setup(self, request, *args, **kwargs):
#         super().setup(request, *args, **kwargs)
#         # self.album_instance = get_object_or_404(Album, pk=self.kwargs['pk'])
#         self.image_inlineformset_factory = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
#         # album_form = AlbumForm(request.POST or None, request.FILES or None)
#         self.image_formset = self.image_inlineformset_factory(instance=self.get_object())
#         # type(self).form_class = self.image_inlineformset_factory #self.album_formset
#         self.extra_context = {'image_formset': self.image_formset}
#         # self.images = request.FILES.getlist('picture')
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         # kwargs['instance'] = self.album_instance
#         return kwargs
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['album_formset'] = self.album_formset
#     #     return context
#     # def get(self, request, *args, **kwargs):
#     #     return render(request,'album/album_form_html.html',context={'album_formset':self.album_formset})
#
#     # def post(self, request, *args, **kwargs):
#     #     album_formset = self.ImageFormSet_1(request.POST, request.FILES, instance=self.album_instance)
#     #     form = self.get_form()
#     #     if form.is_valid():
#     #         form.save()
#     #         files = request.FILES.getlist('picture')
#     #         for image in files:
#     #             image = Image(image=image, album=self.album_instance)
#     #             image.save()
#     #         return self.form_valid(form)
#     #     else:
#     #         return self.form_invalid(form)
#
#     # if album_formset.is_valid():
#     # album_formset.save()
#     #
#     # files = request.FILES.getlist('picture')
#     # for image in files:
#     #     image = Image(image=image, album=self.album_instance)
#     #     image.save()
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#
#         image_inlineformset_factory = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
#         # album_form = AlbumForm(request.POST or None, request.FILES or None)
#         image_formset = image_inlineformset_factory(request.POST, request.FILES, instance=self.object)
#         # type(.form_class = image_inlineformset_factory #album_formset
#         extra_context = {'album_formset': image_formset}
#
#         form_list = [form, image_formset]
#         if all([form.is_valid() for form in form_list]):
#             image_formset.save()
#             for image in request.FILES.getlist('images'):
#                 image = Image(image=image, album=self.object)
#                 image.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


class AlbumEdit(TemplateView):
    template_name = 'album/cbv/album_form_html.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.album_instance = get_object_or_404(Album, pk=self.kwargs['pk'])
        album_form = AlbumForm(request.POST or None, request.FILES or None)
        image_inlineformset_factory = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
        image_formset = image_inlineformset_factory(request.POST or None,
                                                    request.FILES or None,
                                                    instance=self.album_instance)

        self.forms = {'album_form': album_form,
                      'image_formset': image_formset}

        self.extra_context = self.forms

    def post(self, request, *args, **kwargs):

        if all([form.is_valid() for form in self.forms.values()]):
            self.forms['image_formset'].save()
            for image in request.FILES.getlist('images'):
                image = Image(image=image, album=self.album_instance)
                image.save()
        # context = self.get_context_data(**kwargs)
        # return self.render_to_response(context)
        return HttpResponseRedirect(reverse('albumEdit', kwargs={'pk': self.kwargs['pk']}))

    def process_froms(self, request):
        self.setup(request)

        if all([form.is_valid() for form in self.forms.values()]):
            self.forms['image_formset'].save()
            for image in request.FILES.getlist('images'):
                image = Image(image=image, album=self.album_instance)
                image.save()


# class AlbumMixin2:
#     def __init__(self):
#         # super().__init__()
#         # check if base has album
#         if not hasattr(self.model, 'album_id'):
#             #raise raise error, possibly album_id doent exist if 'None'
#             raise Exception
#
#     def form_valid(self, form):
#         self.object = form.save()
#
#         if self.object.album is None:
#             self.object.album = Album.objects.create()
#
#         self.object = form.save()
#         super().form_valid(form)
#
#
# class AlbumMixin():
#     # template_name = 'album/cbv/album_form_html.html'
#
#     def setup(self, request, *args, **kwargs):
#         super().setup(request, *args, **kwargs)
#         self.object = self.get_object()
#         # self.album_instance = get_object_or_404(Album, pk=self.kwargs['pk'])
#
#         self.album_instance = self.object.album
#         album_form = AlbumForm(request.POST or None, request.FILES or None)
#         image_inlineformset_factory = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
#         image_formset = image_inlineformset_factory(request.POST or None,
#                                                     request.FILES or None,
#                                                     instance=self.album_instance)
#
#         self.forms = {'album_form': album_form,
#                       'image_formset': image_formset}
#
#         self.extra_context = self.forms
#
#     def post(self, request, *args, **kwargs):
#
#         self.forms['form'] = self.get_form()
#         if all([form.is_valid() for form in self.forms.values()]):
#             self.forms['image_formset'].save()
#             self.forms['form'].save()
#             for image in request.FILES.getlist('images'):
#                 image = Image(image=image, album=self.album_instance)
#                 image.save()
#         # context = self.get_context_data(**kwargs)
#         # return self.render_to_response(context)
#         return HttpResponseRedirect(reverse('restorerUpdate_cbv', kwargs={'pk': self.kwargs['pk']}))
#
#         # self.success_url = reverse_lazy('restorerUpdate_cbv', kwargs={'pk': self.pk})
#         # return super().post(request, *args, **kwargs)
#     # def process_froms(self, request):
#     #     self.setup(request)
#     #
#     #     if all([form.is_valid() for form in self.forms.values()]):
#     #         self.forms['image_formset'].save()
#     #         for image in request.FILES.getlist('images'):
#     #             image = Image(image=image, album=self.album_instance)
#     #             image.save()
#
#
# @csrf_exempt
# def album_edit_html(request, pk):
#     album_instance = get_object_or_404(Album, pk=pk)
#     ImageFormSet_1 = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
#     # album_form = AlbumForm(request.POST or None, request.FILES or None)
#     album_formset = ImageFormSet_1(instance=album_instance)
#
#     if request.method == 'POST':
#
#         files = request.FILES.getlist('picture')
#         for image in files:
#             image = Image(image=image, album=album_instance)
#             image.save()
#
#         album_formset = ImageFormSet_1(request.POST, request.FILES, instance=album_instance)
#         if album_formset.is_valid():
#             album_formset.save()
#             # return HttpResponseRedirect(reverse('albumDetail', kwargs={'pk': pk}))
#             return HttpResponseRedirect(reverse('album_edit1', kwargs={'pk': pk}))
#
#     # t = loader.get_template('album/album_form_html.html')
#     # c = Context({'album_form_html': album_form})
#     # c1 = {'album_form_html': album_form}
#     # h = t.render({'album_form_html': album_form})
#     # h1 = t.render(c1, request)
#     # return h
#     # def render(request, template_name, context=None, content_type=None, status=None, using=None):
#     # h2 = render(request,'album/album_form_html.html',context={'album_form': album_form})
#     # return h1
#     return render(request, 'album/album_form_html.html', context={'album_formset': album_formset})
#
#
# @csrf_exempt
# def album_edit_html2(request, pk):
#     album_instance = get_object_or_404(Album, pk=pk)
#     ImageFormSet_1 = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
#     # ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': PictureWidget, })
#     album_form = AlbumForm(request.POST or None, request.FILES or None)
#     album_formset = ImageFormSet_1(instance=album_instance)
#
#     if request.is_ajax():
#         album_formset = ImageFormSet_1(request.POST, request.FILES, instance=album_instance)
#         if album_formset.is_valid() and album_form.is_valid():
#             album_formset.save()
#             album_process_form(request, album_instance)
#             album_formset = ImageFormSet_1(instance=album_instance)
#         ttt = album_formset.as_table() + album_form.as_table()
#         return JsonResponse({'success': True, 'album_form': ttt})
#
#     else:
#         t = loader.get_template('album/album_form2.html')
#         c = Context({'album_form': album_form})
#         c1 = {'album_form': album_form}
#         h = t.render({'album_form': album_form})
#         h1 = t.render(c1, request)
#         # return h
#         # def render(request, template_name, context=None, content_type=None, status=None, using=None):
#         h2 = render(request, 'album/album_form2.html', context={'album_form': album_form})
#         # return h1
#         return render(request, 'album/album_form2.html',
#                       context={'album_form': album_form, 'album_formset': album_formset})
#
#
# @csrf_exempt
# def album_edit_ajax(request, pk):
#     album_instance = get_object_or_404(Album, pk=pk)
#     ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm)
#     # ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': PictureWidget, })
#     album_form = AlbumForm(request.POST or None, request.FILES or None)
#
#     if request.is_ajax():
#
#         if request.method == 'GET':
#             album_formset = ImageFormSet(instance=album_instance)
#         # if request.POST['initial'] == 'True':
#         #     album_formset = ImageFormSet(instance=album_instance)
#         #     html = render(request, 'album/album_ajax_form.html',
#         #                   {'album_formset': album_formset, 'album_form': album_form})
#         #     t = loader.get_template('album/album_ajax_form.html')
#         #     c = Context({'album_formset': album_formset, 'album_form': album_form})
#         #     h = t.render({'album_formset': album_formset, 'album_form': album_form})
#         #     return JsonResponse({'success': True, 'album_form': h})
#         #
#         # if request.POST['initial'] == 'False':
#
#         if request.method == 'POST':
#             album_formset = ImageFormSet(request.POST, request.FILES, instance=album_instance)
#             if album_formset.is_valid() and album_form.is_valid():
#                 album_formset.save()
#                 album_process_form(request, album_instance)
#                 album_formset = ImageFormSet(instance=album_instance)
#
#         # html = render(request, 'album/album_form3.html',
#         #               {'album_formset': album_formset, 'album_form': album_form})
#         t = loader.get_template('album/album_ajax_form.html')
#         c = Context({'album_formset': album_formset, 'album_form': album_form})
#         h = t.render({'album_formset': album_formset, 'album_form': album_form})
#         return JsonResponse({'success': True, 'album_ajax_form': h})
#
#     else:
#         t = loader.get_template('album/album_form33.html')
#         c = Context({'album_form': album_form})
#         c1 = {'album_form': album_form}
#         h = t.render({'album_form': album_form})
#         h1 = t.render(c1, request)
#         # return h
#         # def render(request, template_name, context=None, content_type=None, status=None, using=None):
#         h2 = render(request, 'album/album_form3.html', context={'album_form': album_form})
#
#         return render(request, 'album/album_form3.html', context={'album_form': album_form})
#
#
# def album_edit_html_is_valid(request):
#     ImageFormSet = inlineformset_factory(Album, Image, extra=0, form=ImageForm, widgets={'image': PictureWidget, })
#     album_form = AlbumForm(request.POST or None, request.FILES or None)
#     return album_form.is_valid()
#
#
# def test_list(request, pk):
#     image = get_object_or_404(Image, pk=pk)
#     return render(request, 'album/single_image_tmpl.html', {'image': image})
#
#
# def test_detail(request, pk):
#     test = get_object_or_404(Test, pk=pk)
#     return render(request, 'album/test_detail.html', {'test': test})
#
#
# def test_create(request):
#     form = TestForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save()
#         files = request.FILES.getlist('pictures')
#         for image in files:
#             image = Image(image=image, album=instance)
#             image.save()
#         return HttpResponseRedirect(reverse('testList'))
#
#     return render(request, 'album/test_form.html', {'form': form})
#
#
# def test_edit(request, pk):
#     test = get_object_or_404(Test, pk=pk)
#     form = TestForm(request.POST or None, request.FILES or None, instance=test)
#     album = test.album
#     if form.is_valid():
#         form.save()
#         # instance = form.save()
#         # files = request.FILES.getlist('pictures')
#         # for image in files:
#         #     image = Image(image=image, album=instance)
#         #     image.save()
#         return HttpResponseRedirect(reverse('testList'))
#
#     return render(request, 'album/test_form.html', {'form': form, 'album_id': getattr(test.album, 'id', None)})
#
#
# class TestListView(generic.ListView):
#     model = Test
#     paginate_by = 10
#
#
# class TestCreateView(generic.CreateView):
#     model = Test
#     fields = '__all__'
#
#
# class TestDetailView(generic.DetailView):
#     model = Album
#
#     #
#     # if request.method == 'POST':
#     #     album_formset = ImageFormSet(request.POST, request.FILES, instance=album_instance)
#     #     if album_formset.is_valid() and album_form.is_valid():
#     #         album_formset.save()
#     #         album_process_form(request, album_instance)
#     #         return HttpResponseRedirect(reverse('monumentList'))
#     #     else:
#     #         return render(request, 'album/album_form.html', {'album_formset': album_formset, 'album_form': album_form})
#     #
#     # album_formset = ImageFormSet(instance=album_instance)
#     # return render(request, 'album/album_form.html', {'album_formset': album_formset, 'album_form': album_form})
#
# # def album_edit(album, image_dev_id="album", edit=False):
# #     if image_dev_id is None:
# #         image_dev_id = 'album_id_%s' % album.id
# #     htmlDivContent = ['<div id = %s>' % image_dev_id]
# #     for image in album.imageList.all():
# #         htmlDivContent.append('<p> %s </p>' % image.name)
# #         htmlDivContent.append('<figure>'
# #                                 '<image src=%s><figcaption> %s </figcaption>'
# #                               '</figure>' % (image.image.url, 'test'))
# #     return '\n'.join(htmlDivContent)
