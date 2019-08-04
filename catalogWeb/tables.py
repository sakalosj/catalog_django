from random import randint

import django_tables2 as tables

from catalogWeb.models import Person, Monument


class PersonTable(tables.Table):
    # edit = tables.Column('test',linkify=lambda person_edit:,orderable=False)
    # test = tables.Column('testttt',empty_values=(22,))
    # edit = tables.TemplateColumn('<a href="{% url "personUpdate" record.pk %}">edit</a>', verbose_name='')
    # edit2 = tables.Column(default='e',linkify=('personUpdate', {'pk':1}))
    # delete = tables.TemplateColumn('<a href="{% url "personDelete" record.pk %}">delete</a>', verbose_name='')
    actions = tables.TemplateColumn('<a href="{% url "personUpdate" record.pk %}">edit</a>/<a href="{% url "personDelete" record.pk %}">delete</a>', verbose_name='')
    # album = tables.Column(linkify=True)
    full_name = tables.Column(verbose_name='Name', order_by=('last_name', 'first_name'),linkify=('personDetail',{'pk': tables.A('pk')}))
    # full_name = tables.TemplateColumn('<a href="{% url "personDetail" record.pk %}">record.full_name</a>', verbose_name='')


    class Meta:
        model = Person
        # exclude = ('person2user', 'album','id')
        fields = ('full_name', 'description', 'actions')
        # sequence = ()


class MonumentTable(tables.Table):


    class Meta:
        model = Monument
        # exclude = ()
        fields = ('name', 'author', 'description', 'owner')