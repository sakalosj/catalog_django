from datetime import datetime
from random import randint

from catalogWeb.models import Role, Person, Monument


def populate_roles():
    for name in ['restorer', 'grant', 'company']:
        Role(name=name).save()


def populate_person():
    person = []
    for name in [('a', 'a'), ('b', 'b'), ('c', 'c')]:
        person.append(Person(first_name=name[0], last_name=name[1]))
        person[-1].save()

    person[0].roles.set(['restorer', 'grant'])
    person[1].roles.set(['restorer', 'grant', 'company'])
    person[2].roles.set([])


def populate_monument():
    for i in range(5):
        m = Monument(name='name' + str(i),date=datetime.now())
        m.save()
        for x in range(randint(0, 3)):
            sub_m = Monument(name='name_sub_' + str(x), description='sub of '+ str(i), date=datetime.now())
            sub_m.save()
            m.related_monuments.add(sub_m)


def run_all():
    populate_roles()
    populate_person()
