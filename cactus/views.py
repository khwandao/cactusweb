from django import template
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Species, Cacti
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

'''
def home(request):
    
    
    return render(request, 'cactus/home.html', {'name':'kapom'})
'''


def home(request):
    species_list = Species.objects.order_by('name')

    template = loader.get_template('cactus/home.html')
    context = {
        'species_list': species_list,
    }
    return HttpResponse(template.render(context, request))


    '''
    return render(
        request, 
        'cactus/home.html', 
        {'species_list': species_list,}
    )
    '''

def detail(request, species_id):
    return HttpResponse('hello')




