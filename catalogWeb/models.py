import re

import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.forms import Widget, Select
from django.urls import reverse
from django.utils import six, datetime_safe
from django.utils.dates import MONTHS
from django.utils.encoding import force_text, force_str
from django.utils.formats import get_format


# Create your models here.
# class AlbumReferenceMixin:
#     def save(self):
#         if hasattr(self, 'album_id'):  # check if model has set album attribute (related to onetoone implementation)
#             if not hasattr(self, 'album'):  # check if there is set related object (django specific)
#                 self.album = Album.objects.create()
#         else:
#             raise Exception('Inherited function have to contain property album referencing model Album')
#         super().save()
#
#     def delete(self):
#         if hasattr(self, 'album_id'):  # check if model has set album attribute (related to onetoone implementation)
#             if hasattr(self, 'album'):  # check if there is set related object (django specific)
#                 self.album.delete()
#         super().delete()
from album.models import AlbumMixin

class UrlMmodelMixin:

    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)
        cls.main_menu_name = cls.__name__.lower()

    @classmethod
    def get_list_url(cls):
        return reverse(cls.main_menu_name + 'List')

    @classmethod
    def get_create_url(cls):
        return reverse(cls.main_menu_name + 'Create')

    def get_details_url(self):
        # return reverse(self.main_menu_name + 'Details', self.id)
        return self.get_absolute_url()

    def get_update_url(self):
        return reverse(self.main_menu_name + 'Update', self.id)

    @classmethod
    def get_filter_url(cls):
        return reverse(cls.main_menu_name + 'Filter')

class RestorerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(roles__name__in=['restorer'])




class Person(AlbumMixin, models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    person2user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    roles = models.ManyToManyField('Role')
    album = models.OneToOneField('album.Album', null=True, on_delete=models.SET_NULL)
    # edit_view = 'restorerEdit'
    # update_view = 'restorerUpdate'
    objects = models.Manager()
    restorers = RestorerManager()

    @property
    def full_name(self):
        return '{}, {}'.format(self.last_name, self.first_name)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Role(models.Model):
    name = models.CharField(max_length=30, primary_key=True)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name

# class CustomUser(AlbumMixin, User):
#     description = models.CharField(max_length=200, null=True)
#     related_person = models.OneToOneField()
# class Person2Role(models.Model):
#     person = models.ForeignKey('Person', null=True, on_delete=models.SET_NULL)
#     role = models.ForeignKey('Role', null=True, on_delete=models.SET_NULL)
#     # materialList = models.OneToOneField('MaterialList', on_delete=models.PROTECT)
#     # testfield = models.CharField(max_length=45)

class Monument(AlbumMixin, models.Model):
    name = models.CharField(max_length=45)
    author = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45)
    date = models.DateField(blank=True, null=True)
    placement = models.CharField(max_length=45, blank=True, null=True)
    provenance = models.CharField(max_length=45)
    owner = models.CharField(max_length=45, blank=True, null=True)
    dimensions = models.CharField(max_length=45)
    technique = models.CharField(max_length=45)
    materials = models.ManyToManyField('Material', through='Monument2Material',
                                        # through_fields=('materialList', 'material')
                                        blank=True)
    # related_monuments = models.ManyToManyField('Monument', blank=True)
    parent_monument = models.ForeignKey('Monument', blank=True, null=True, on_delete=models.SET_NULL)
    # album = models.OneToOneField('album.Album', null=True, on_delete=models.CASCADE)
    # album = models.OneToOneField('album.Album', null=True, on_delete=models.SET_NULL)

    album_before = models.OneToOneField('album.Album', related_name='album_1_rel', null=True, on_delete=models.SET_NULL)
    album_after = models.OneToOneField('album.Album',  related_name='album_2_rel', null=True, on_delete=models.SET_NULL)


    def get_absolute_url(self):
        return reverse('monumentDetail', args=(self.id,))

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name


class Monument2Project(models.Model):
    monument = models.ForeignKey(Monument, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    # materialList = models.OneToOneField('MaterialList', on_delete=models.PROTECT)
    testfield = models.CharField(max_length=45)


class Monument2Material(models.Model):
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    monument = models.ForeignKey('Monument', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)  # project specific info


class ResearchRelation(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, null=True)
    monument = models.ForeignKey(Monument, on_delete=models.PROTECT, blank=True, null=True)
    research = models.ForeignKey('Research', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=200)


class Project(models.Model):
    name = models.CharField(max_length=45)
    garant = models.ForeignKey('Person', on_delete=models.DO_NOTHING, related_name='garant_for')
    description = models.CharField(max_length=200)
    realized_by = models.CharField(max_length=45)
    realized_for = models.CharField(max_length=45)
    restorerList = models.ManyToManyField(Person, blank=True)
    monument_list = models.ManyToManyField(Monument, blank=True, through=Monument2Project)

    def get_absolute_url(self):
        return reverse('projectDetail', args=(self.id,))

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name


class Material(AlbumMixin, models.Model):
    # MaterialDefinition = models.ForeignKey('MaterialDefinition')
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)  # general info
    # album = models.OneToOneField('album.Album', null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('materialDetail', args=(self.id,))

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name  # self.MaterialDefinition.name


class Research(AlbumMixin, models.Model):
    PLANNING = 'pl'
    ONGOING = 'on'
    FINISHED = 'fi'

    STATUS = [
        (PLANNING, 'Planning in progress'),
        (ONGOING, 'Work in progress'),
        (FINISHED, 'Work finished'),
    ]

    # monument = models.ForeignKey(Monument, blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)  # general info
    date = models.DateField(blank=True, null=True)
    monument = models.ManyToManyField(Monument, blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    UVA = models.BooleanField()
    UVC = models.BooleanField()
    RUVA = models.BooleanField()
    IR = models.BooleanField()
    RTG = models.BooleanField()
    CT = models.BooleanField()
    CT_date = models.DateField(blank=True, null=True)
    CT_description = models.TextField(blank=True, null=True)
    ch_t_research = models.BooleanField()
    sondazny = models.CharField(max_length=200)
    other = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=STATUS, default=PLANNING)
    # album = models.OneToOneField('album.Album', null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('researchDetail', args=(self.id,))

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % self.name

# class ResearchManager(models.Manager):
#     def create_research(self, project, monuments):
#         research =  self.create(project=project)

############################################################


############################################################


# class Image(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='pictures/')
#     album = models.ForeignKey('Album', related_name='imageList', blank=True, null=True, on_delete=models.CASCADE)
#
#
# class Album(models.Model):
#     def as_div(self, imageDivID="album"):
#         if imageDivID is None:
#             imageDivID = 'album_id_%s' % self.id
#         htmlDivContent = ['<div id = %s>' % self]
#         for image in self.imageList.all():
#             htmlDivContent.append('<p> %s </p>' % image.name)
#             htmlDivContent.append('<image src=%s>' % image.image.url)
#         return '\n'.join(htmlDivContent)
#
#     def __str__(self):
#         """
#         String for representing the Model object.
#         """
#         return 'album_id_%s' % self.id

###################################################################################
###################################################################################
###################################################################################


class SelectDateWidget2(Widget):
    """
    A Widget that splits date input into three <select> boxes.

    This also serves as an example of a Widget that has more than one HTML
    element and hence implements value_from_datadict.
    """
    none_value = (0, '---')
    month_field = '%s_month'
    day_field = '%s_day'
    year_field = '%s_year'
    template_name = 'django/forms/widgets/select_date.html'
    input_type = 'select'
    select_widget = Select
    date_re = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')

    def __init__(self, attrs=None, years=None, months=None, empty_label=None):
        self.attrs = attrs or {}

        # Optional list or tuple of years to use in the "year" select box.
        if years:
            self.years = years
        else:
            this_year = datetime.date.today().year
            self.years = range(this_year, this_year + 10)

        # Optional dict of months to use in the "month" select box.
        if months:
            self.months = months
        else:
            self.months = MONTHS

        # Optional string, list, or tuple to use as empty_label.
        if isinstance(empty_label, (list, tuple)):
            if not len(empty_label) == 3:
                raise ValueError('empty_label list/tuple must have 3 elements.')

            self.year_none_value = (0, empty_label[0])
            self.month_none_value = (0, empty_label[1])
            self.day_none_value = (0, empty_label[2])
        else:
            if empty_label is not None:
                self.none_value = (0, empty_label)

            self.year_none_value = self.none_value
            self.month_none_value = self.none_value
            self.day_none_value = self.none_value

    def get_context(self, name, value, attrs):
        context = super(SelectDateWidget2, self).get_context(name, value, attrs)
        date_context = {}
        year_choices = [(i, force_text(i)) for i in self.years]
        if self.is_required is False:
            year_choices.insert(0, self.year_none_value)
        year_attrs = context['widget']['attrs'].copy()
        year_name = self.year_field % name
        year_attrs['id'] = 'id_%s' % year_name
        date_context['year'] = self.select_widget(attrs, choices=year_choices).get_context(
            name=year_name,
            value=context['widget']['value']['year'],
            attrs=year_attrs,
        )
        month_choices = list(self.months.items())
        if self.is_required is False:
            month_choices.insert(0, self.month_none_value)
        month_attrs = context['widget']['attrs'].copy()
        month_name = self.month_field % name
        month_attrs['id'] = 'id_%s' % month_name
        date_context['month'] = self.select_widget(attrs, choices=month_choices).get_context(
            name=month_name,
            value=context['widget']['value']['month'],
            attrs=month_attrs,
        )
        day_choices = [(i, i) for i in range(1, 32)]
        if self.is_required is False:
            day_choices.insert(0, self.day_none_value)
        day_attrs = context['widget']['attrs'].copy()
        day_name = self.day_field % name
        day_attrs['id'] = 'id_%s' % day_name
        date_context['day'] = self.select_widget(attrs, choices=day_choices,).get_context(
            name=day_name,
            value=context['widget']['value']['day'],
            attrs=day_attrs,
        )
        subwidgets = []
        for field in self._parse_date_fmt():
            subwidgets.append(date_context[field]['widget'])
        context['widget']['subwidgets'] = subwidgets
        return context

    def format_value(self, value):
        """
        Return a dict containing the year, month, and day of the current value.
        Use dict instead of a datetime to allow invalid dates such as February
        31 to display correctly.
        """
        year, month, day = None, None, None
        if isinstance(value, (datetime.date, datetime.datetime)):
            year, month, day = value.year, value.month, value.day
        elif isinstance(value, six.string_types):
            if settings.USE_L10N:
                try:
                    input_format = get_format('DATE_INPUT_FORMATS')[0]
                    d = datetime.datetime.strptime(force_str(value), input_format)
                    year, month, day = d.year, d.month, d.day
                except ValueError:
                    pass
            match = self.date_re.match(value)
            if match:
                year, month, day = [int(val) for val in match.groups()]
        return {'year': year, 'month': month, 'day': day}

    @staticmethod
    def _parse_date_fmt():
        fmt = get_format('DATE_FORMAT')
        escaped = False
        for char in fmt:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char in 'Yy':
                yield 'year'
            elif char in 'bEFMmNn':
                yield 'month'
            elif char in 'dj':
                yield 'day'

    def id_for_label(self, id_):
        for first_select in self._parse_date_fmt():
            return '%s_%s' % (id_, first_select)
        else:
            return '%s_month' % id_

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        d = data.get(self.day_field % name)
        if y == m == d == "0":
            return None
        if y and m and d:
            if settings.USE_L10N:
                input_format = get_format('DATE_INPUT_FORMATS')[0]
                try:
                    date_value = datetime.date(int(y), int(m), int(d))
                except ValueError:
                    return '%s-%s-%s' % (y, m, d)
                else:
                    date_value = datetime_safe.new_date(date_value)
                    return date_value.strftime(input_format)
            else:
                return '%s-%s-%s' % (y, m, d)
        return data.get(name)

    def value_omitted_from_data(self, data, files, name):
        return not any(
            ('{}_{}'.format(name, interval) in data)
            for interval in ('year', 'month', 'day')
        )




