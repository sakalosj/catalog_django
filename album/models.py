from django.db import models

# Create your models here.
from django.forms import modelform_factory, inlineformset_factory


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='pictures/')
    album = models.ForeignKey('Album', related_name='imageList', blank=True, null=True, on_delete=models.CASCADE)


class Album(models.Model):

    def as_div(self, imageDivID="album"):
        if imageDivID is None:
            imageDivID = 'album_id_%s' % self.id
        htmlDivContent = ['<div id = %s>' % self]
        for image in self.imageList.all():
            htmlDivContent.append('<p> %s </p>' % image.name)
            htmlDivContent.append('<image src=%s>' % image.image.url)
        return '\n'.join(htmlDivContent)

    def generate_formset(self, *args, **kwargs):
        return self.ImageFormSet(*args, **kwargs)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return 'album_id_%s' % self.id


class AlbumMixin:
    def save(self, *args, **kwargs):
        if hasattr(self, 'album_id'):  # check if model has set album attribute (related to onetoone implementation)
            # if not hasattr(self, 'album'):  # check if there is set related object (django specific)
            if self.album is None:
                self.album = Album.objects.create()
        else:
            raise Exception('AlbumMixin Inherited function have to contain property album referencing model Album')
        super().save(*args, **kwargs)

    def delete(self):
        if hasattr(self, 'album_id'):  # check if model has set album attribute (related to onetoone implementation)
            if self.album is not None:  # check if there is set related object (django specific)
                self.album.delete()
        super().delete()
