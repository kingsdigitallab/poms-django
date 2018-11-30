# Create your views here.

from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render

from pomsapp.models import Place


def map_view(request):
    return render(request, 'pomsapp/map/map.html', {})


def map_image(request):
    imageStr = request.POST.get('image', False)
    context = {}
    context['imageStr'] = imageStr
    return render(request, 'pomsapp/map/map_image.html', context)
    # return
    # HttpResponseRedirect('pomsapp/map/map_image.html',
    # context,context_instance=RequestContext(request))


def map_search(request):
    geomPoly = GEOSGeometry(
        '{ "type": "Polygon", "coordinates":' +
        request.GET.get('selected_geom') +
        '}}')
    context = {}
    context['places'] = Place.objects.filter(
        geom__intersects=geomPoly).exclude(
        parent__isnull=True)
    return render(request, 'pomsapp/map/map_results.js',
                  context, content_type='application/json')


def map_search_by_parent(request):
    from itertools import chain
    id = request.GET.get('id', '')
    context = {}
    # Check 3 levels of hierarchy
    results_list = list(chain(Place.objects.filter(parent__id=id),
                              Place.objects.filter(parent__parent__id=id),
                              Place.objects.filter(
                                  parent__parent__parent__id=id)))
    context['places'] = results_list
    return render(request, 'pomsapp/map/map_results.js',
                  context, content_type='application/json')


def hierarchy(request):
    # get places with children and without parents and order alphabetically
    places = Place.objects.exclude(
        parent__isnull=False).filter(
        name__contains='(')  # .order_by('name')
    places = places | Place.objects.exclude(
        parent__isnull=False).filter(
        name__contains='/')
    places = places.exclude(pk=2054).exclude(pk=3652)
    places = places.order_by('name')
    # places = Place.objects.exclude(parent__isnull=False).order_by('name')
    context = {}
    context['places'] = places
    return render(request, 'pomsapp/map/parent_places.html', context)
