from random import randint

import django_tables2 as tables

from catalogWeb.models import Person

def rrr():
    return randint(1,100)

class PersonTable(tables.Table):
    # edit = tables.Column('test',linkify=lambda person_edit:,orderable=False)
    # test = tables.Column('testttt',empty_values=(22,))
    # edit1 = tables.Column(default=rrr,linkify=('personUpdate', {'pk':1}))
    edit = tables.TemplateColumn('<a href="{% url "personUpdate" record.pk %}">edit</a>', verbose_name='')
    # album = tables.Column(linkify=True)
    full_name = tables.Column(verbose_name='Name', order_by=('last_name', 'first_name'))


    class Meta:
        model = Person
        # exclude = ('person2user', 'album','id')
        fields = ('full_name', 'description', 'edit')
        # sequence = ()