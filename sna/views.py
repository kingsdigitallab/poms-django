# Create your views here.

from django.shortcuts import render


from sna.models import GephiVis


def sna_all(request, id):
    context = {}
    context['visualisations'] = GephiVis.objects.all()
    context['viz'] = GephiVis.objects.get(pk=id)
    return render(request, 'sna_all.html', context)


def sna_default(request):
    context = {}
    context['visualisations'] = GephiVis.objects.all()
    context['viz'] = GephiVis.objects.all()[0]
    return render(request, 'sna_all.html', context)


def sna_js(request, id, style):
    context = {}
    context['viz'] = GephiVis.objects.get(pk=id)

    if style == 'curvy':
        return render(request, 'config_curvy.js', context,
                      content_type='application/json')
    if style == 'straight':
        return render(request, 'config_straight.js', context,
                      content_type='application/json')


def sna_person(request, id):
    # Very simple view to render SNA page with a tiny snippet of 'doc ready'
    # in order to focus the gephi graph on an individual
    context = {}
    context['person_id'] = id
    context['type'] = 'family'
    return render(request,'sna_person.html', context)


def sna_person_base(request):
    context = {}
    context['type'] = 'family'
    return render(request,'sna.html', context)


def sna_grantor(request, id):
    # Very simple view to render SNA page with a tiny snippet of 'doc ready'
    # in order to focus the gephi graph on an individual
    context = {}
    context['person_id'] = id
    context['type'] = 'grantor'
    return render(request,'sna_grantor_person.html', context)


def sna_grantor_base(request):
    context = {}
    context['type'] = 'grantor'
    return render(request,'sna_grantor.html', context)
