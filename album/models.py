from django.db import models

# Create your models here.
from django.forms import modelform_factory, inlineformset_factory

from album import fields
from album.widgets import PictureWidget


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='pictures/')
    album = models.ForeignKey('Album', related_name='imageList', blank=True, null=True, on_delete=models.CASCADE)


    def formfield(self, **kwargs):
        return

class Image2(models.Model):
    name = models.CharField(max_length=255, blank=True)
    picture = fields.PictureFields()
    album = models.ForeignKey('Album', related_name='imageList2', blank=True, null=True, on_delete=models.CASCADE)



class Album(models.Model):

    def as_div(self, imageDivID="album"):
        if imageDivID is None:
            imageDivID = 'album_id_%s' % self.id
        htmlDivContent = ['<div id = %s>' % self]
        for image in self.imageList.all():
            htmlDivContent.append('<p> %s </p>' % image.name)
            htmlDivContent.append('<image src=%s>' % image.image.url)
        return '\n'.join(htmlDivContent)

    def generate_forms(self, *args, **kwargs):
        return self.ImageFormSet(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('albumDetail', args=[str(self.id)])

    # def get_forms(self):



    def __str__(self):
        """
        String for representing the Model object.
        """
        return 'album_id_%s' % self.id


class Test(models.Model):

    name = models.CharField(max_length=255, blank=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return 'test_%s' % self.id

class AlbumMixin(models.Model):
    """

    """

    album = models.OneToOneField('album.Album', null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(self, 'album_id'):  # check if model has set album attribute (related to onetoone implementation)
            # if not hasattr(self, 'album'):  # check if there is set related object (django specific)
            raise Exception('AlbumMixin Inherited function have to contain property album referencing model Album')

    def save(self, *args, **kwargs):
        if self.album is None:
            self.album = Album.objects.create()
        super().save(*args, **kwargs)

    # def delete(self):
    #     if hasattr(self, 'album_id'):  # check if model has set album attribute (related to onetoone implementation)
    #         if self.album is not None:  # check if there is set related object (django specific)
    #             self.album.delete()
    #     super().delete()
