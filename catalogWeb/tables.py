from random import randint

import django_tables2 as tables

from catalogWeb.models import Person, Monument, Research, Project, Material


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

class ProjectTable(tables.Table):
    name = tables.Column(linkify=True)
    actions = tables.TemplateColumn('<a href="{% url "projectUpdate" record.pk %}">edit</a>/<a href="{% url "projectDelete" record.pk %}">delete</a>', verbose_name='')
    # full_name = tables.Column(verbose_name='Name', order_by=('last_name', 'first_name'),linkify=('projectDetail',{'pk': tables.A('pk')}))

    class Meta:
        model = Project
        fields = ('name', 'description', 'status')

class MonumentTable(tables.Table):

    name = tables.Column(linkify=True)

    actions = tables.TemplateColumn('<a href="{% url "monumentUpdate" record.pk %}">edit</a>/<a href="{% url "monumentDelete" record.pk %}">delete</a>', verbose_name='')

    class Meta:
        model = Monument
        # exclude = ()
        fields = ('name', 'author', 'description', 'owner')


class ResearchTable(tables.Table):

    name = tables.Column(linkify=True)

    actions = tables.TemplateColumn('<a href="{% url "researchUpdate" record.pk %}">edit</a>/<a href="{% url "researchDelete" record.pk %}">delete</a>', verbose_name='')

    class Meta:
        model = Research
        # exclude = ()
        fields = ('name', 'author', 'description', 'owner')


class MaterialTable(tables.Table):

    name = tables.Column(linkify=True)

    actions = tables.TemplateColumn('<a href="{% url "materialUpdate" record.pk %}">edit</a>/<a href="{% url "materialDelete" record.pk %}">delete</a>', verbose_name='')

    class Meta:
        model = Material
        # exclude = ()
        fields = ('name', 'author', 'description', 'owner')
