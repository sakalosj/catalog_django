from datetime import datetime

from django.urls import reverse
from django.views.generic.base import ContextMixin
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseCreateView, BaseUpdateView
from django.views.generic.list import BaseListView
from django_filters.views import FilterView


class GenericTemplateMenuMixin(ContextMixin):
    pass
    TEST_V = None

    # def get_context_data(self, **kwargs):
    #     url_dict = {'list_url': self.get_list_url(),
    #                 }
    #     if kwargs:
    #         url_dict.update(kwargs)
    #     return super().get_context_data(url_dict)

    def get_context_data(self, **kwargs):
        self.__class__.TEST_V = datetime.now()
        print(self.__class__.TEST_V)
        return super().get_context_data(**kwargs)


class UrlViewMixin(ContextMixin):
    cnt = 0

    # main_menu_name = __class__.__name__.lower()
    def __init_subclass__(cls, menu_section=None, *args, **kwargs):
        if not getattr(cls, 'model', None):
            raise Exception('UrlMixin: model attribute not defined in parent class')
        super().__init_subclass__(*args, **kwargs)
        cls.main_menu_name = cls.model.__name__.lower()

    def __init__(self):
        self.__class__.cnt += 1

        def get_section():
            if issubclass(type(self),BaseListView):
                return 'list'
            if issubclass(type(self),BaseCreateView):
                return 'create'
            if issubclass(type(self),BaseUpdateView):
                return 'update'
            if issubclass(type(self),BaseDetailView):
                return 'detail'
            if issubclass(type(self),FilterView):
                return 'filter'

        self.sidebar_section = get_section()
        self.urls = None

    # def __init__(self, *args, **kwargs):
    #
    #     if not getattr(self, 'main_menu_name', None):
    #         # setattr(self, 'main_menu_name', self.__class__.__name__.lower())
    #         self.main_menu_name = self.__class__.__name__.lower()
    #
    #     super().__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        self.urls = {
            'list_url': reverse(self.main_menu_name + 'List'),
            'create_url': reverse(self.main_menu_name + 'Create'),
            'filter_url': reverse(self.main_menu_name + 'Filter')
        }
        if hasattr(self, 'get_object'):
            try:
                obj = self.get_object()
            except AttributeError:
                pass
            else:
                self.urls.update({
                    'detail_url': reverse(self.main_menu_name + 'Detail', args=(obj.id,)),
                    'update_url': reverse(self.main_menu_name + 'Update', args=(obj.id,)),
                })

        kwargs.update(self.urls)
        kwargs.update({'sidebar_section': self.sidebar_section, 'main_menu_section': self.main_menu_name})
        return super().get_context_data(**kwargs)

    def get_main_menu_name(self):
        return self.main_menu_name

    def get_absolute_url(self):
        return reverse(self.main_menu_name + 'Details', self.id)

    def get_list_url(self):
        return reverse(self.main_menu_name + 'List')

    def get_create_url(self):
        return reverse(self.main_menu_name + 'Create')

    def get_details_url(self):
        # return reverse(self.main_menu_name + 'Details', self.id)
        return self.get_absolute_url()

    def get_update_url(self):
        return reverse(self.main_menu_name + 'Update', self.id)

    def get_filter_url(self):
        return reverse(self.main_menu_name + 'Filter')
