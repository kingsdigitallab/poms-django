
from django import template
from pomsapp import models

register = template.Library()


# for People template

@register.inclusion_tag('admin/snippets/personfactoid_info.html')
def display_personfactoids(person_id):
    person = models.Person.objects.get(id__exact=person_id)
    # factoids = models.Factoids.objects.filter(people=person)
    return {'person': person}


@register.inclusion_tag('admin/snippets/personwitnessfactoid_info.html')
def display_personwitness(person_id):
    person = models.Person.objects.get(id__exact=person_id)
    # factoids = models.Factoids.objects.filter(people=person)
    return {'person': person}


@register.inclusion_tag('admin/snippets/personproanimafactoid_info.html')
def display_personproanima(person_id):
    person = models.Person.objects.get(id__exact=person_id)
    # factoids = models.Factoids.objects.filter(people=person)
    return {'person': person}


@register.inclusion_tag('admin/snippets/personmatrix_info.html')
def display_personmatrix(person_id):
    person = models.Person.objects.get(id__exact=person_id)
    # factoids = models.Factoids.objects.filter(people=person)
    return {'person': person}


# for Document template


@register.inclusion_tag('admin/snippets/charterfactoids_info.html')
def display_charterfactoids(document_id):
    document = models.Source.objects.get(id__exact=document_id)
    return {'document': document}


# for Place template


@register.inclusion_tag('admin/snippets/placepossessions_info.html')
def display_placepossessions(place_id):
    place = models.Place.objects.get(id__exact=place_id)
    return {'place': place}


@register.inclusion_tag('admin/snippets/placepersons_info.html')
def display_placepersons(place_id):
    place = models.Place.objects.get(id__exact=place_id)
    return {'place': place}


# for Possessions/Privileges template


@register.inclusion_tag('admin/snippets/possession_factoids_info.html')
def display_possessionfactoids(possession_id):
    possession = models.PossessionNew.objects.get(id__exact=possession_id)
    realpossession = possession.get_right_subclass()[1]
    return {'possession': realpossession}


@register.inclusion_tag('admin/snippets/possession_factoids_info.html')
def display_privilegesfactoids(privilege_id):
    privilege = models.Privileges.objects.get(id__exact=privilege_id)
    # shortcut: passing the variale 'possession' so that we can reuse the
    # template...
    return {'possession': privilege}


# for Matrix template


@register.inclusion_tag('admin/snippets/seals_info.html')
def display_seals(document_id):
    matrix = models.Matrix.objects.get(id__exact=document_id)
    return {'record': matrix}
