import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Avg

from test_project.models import Province, Municipality, Zone

def index(request):
    """
    index.html page view logic
    """
    
    return render(request, 'test_project/index.html', {});

def stats(request):
    """
    Return the avg number of provinces and municipalities per zone in HTTP JSON
    """
    avg_provinces_per_zone = Zone.objects \
        .annotate(num_province=Count('province')) \
        .aggregate(average=Avg('num_province'))
    avg_provinces_per_zone = avg_provinces_per_zone['average']
    
    avg_municipality_per_zone = Zone.objects \
        .annotate(num_municipality=Count('province__municipality')) \
        .aggregate(average=Avg('num_municipality'))
    avg_municipality_per_zone = avg_municipality_per_zone['average']
    
    result = {}
    result['avg_prov_per_zone'] = float(avg_provinces_per_zone)
    result['avg_mun_per_zone'] = float(avg_municipality_per_zone)
    
    json_result = json.dumps(result)
    return HttpResponse(json_result, content_type='application/json')

def get_municipalities_json(request, province_code):
    """Return the municipalities of a province_code as JSON in HttpResponse"""
    
    municipalities = []
    if (province_code != ''):
        municipalities_instances = get_municipalities(province_code)
        for a_municipality in municipalities_instances:
            municipalities.append(a_municipality.name)
    
    result = json.dumps(municipalities)
    return HttpResponse(result, content_type='application/json')

def get_municipalities(province_name):
    """Return an iterator of Municipalities associated to a province_name"""
    
    if (province_name != None and province_name != ""):
        province_name = province_name.strip()
        try:
            a_province = Province.objects.get(name__iexact=province_name)
            return a_province.municipality_set.order_by('name')
        except (ObjectDoesNotExist):
            return iter([])
    else:
        return iter([])

def compare_municipality(x, y):
    """Compare whether a Municipality instance is greather than another one.
    
    If the name attribute of instance x is greater than the y (string
    comparison), then 1 is return.
    
    If both are same, return 0
    
    if the name attribute of y is greater than x, returns -1
    """
    
    if (x.name > y.name):
        return 1
    elif (x.name == y.name):
        return 0
    else:
        return -1


        