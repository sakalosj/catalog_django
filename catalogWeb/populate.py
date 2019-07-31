from catalogWeb.models import Role, Person


def populate_roles():
    for name in ['restorer', 'grant', 'company']:
        Role(name=name).save()


def populate_person():
    person = []
    for name in [('a', 'a'), ('b', 'b'), ('c', 'c')]:
        person.append(Person(first_name=name[0], last_name=name[1]))
        person[-1].save()

    person[0].roles.set(['restorer','grant'])
    person[1].roles.set(['restorer','grant','company'])
    person[2].roles.set([])


def run_all():
    populate_roles()
    populate_person()
