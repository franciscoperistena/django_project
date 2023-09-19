from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import Template, Context

# Create your views here.


class Person(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


def foo(request: HttpRequest):

    name = 'Fran'
    surname = 'Peris'
    person = Person(name=name, surname=surname)

    l_person = ['Fran', 'Boryana', 'José Luís']

    template_file = open(file=r'C:\Users\Fran Tena\Documents\django_project\templates\foo.html')

    template = Template(template_file.read())

    template_file.close()

    context = Context(
        {
            'person': person,
            "l_person": l_person
        }
    )
    content = template.render(context=context)

    return HttpResponse(content=content)

