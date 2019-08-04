import os

from django.db import models

from catalog import settings

def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/{0}/{1}'.format(instance.album.id, filename)


class ImageGroup(models.Manager):

    def by_group(self, group):
        return super().get_queryset().filter(image_group=group)


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=image_path)
    album = models.ForeignKey('Album', related_name='imageList', blank=True, null=True, on_delete=models.CASCADE)
    image_group = models.CharField(max_length=30, blank=True, null=True)


    # object = models.Manager()
    object = ImageGroup()
    def formfield(self, **kwargs):
        return

    # def _get_path(self):
    #     if self.album:
    #         return self.album.get_path()
    #     else:
    #         return 'images/'





class Album(models.Model):

    #
    # def as_div(self, imageDivID="album"):
    #     if imageDivID is None:
    #         imageDivID = 'album_id_%s' % self.id
    #     htmlDivContent = ['<div id = %s>' % self]
    #     for image in self.imageList.all():
    #         htmlDivContent.append('<p> %s </p>' % image.name)
    #         htmlDivContent.append('<image src=%s>' % image.image.url)
    #     return '\n'.join(htmlDivContent)

    # def generate_forms(self, *args, **kwargs):
    #     return self.ImageFormSet(*args, **kwargs)
    objects = models.Manager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('albumDetail', args=[str(self.id)])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
        os.mkdir(os.path.join(settings.MEDIA_ROOT, self.get_path()))

    def delete(self, using=None, keep_parents=False):
        path = self.get_path()
        super().delete(using=None, keep_parents=False)
        os.rmdir(os.path.join(settings.MEDIA_ROOT, path))

    def get_path(self):
        try:
            path = 'images/' + str(self.id)
        except:
            raise Exception('error while generating path for album')

        return path

    def get_images_by_group(self, group):
        if group == '__all__':
            return self.imageList.all()
        return self.imageList.filter(image_group=group)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return 'album_id_%s' % self.id


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

    def delete(self, *args, **kwargs):
        if hasattr(self, 'album_id'):  # check if model has set album attribute (related to onetoone implementation)
            if self.album is not None:  # check if there is set related object (django specific)
                self.album.delete()
        super().delete()
