from django import template
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Species, Cacti
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse


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
    try:
        cacti = Cacti.objects.filter(species_id=species_id)        
    except Cacti.DoesNotExist:        
        raise Http404("Cacti does not exist")

    
    for item in cacti:
        species_name = item.species_id.name + " Page"
        break

    return render(request, 'cactus/detail.html', {'cacti': cacti, 'species_name': species_name })


def cacti_detail(request, cactus_id): 

    # ส่งคืนไปค่าเดียวตามพารามิเตอร์ที่รับมา
    try:
        cacti = Cacti.objects.filter(id=cactus_id)
        # select * from cacti where species_id=1
    except Cacti.DoesNotExist:        
        raise Http404("Cacti does not exist")

    for item in cacti:
        species_id = item.species_id
    
    # ส่งคืนทุกค่ายกเว้นพารามิเตอร์ที่รับมา    
    try:
        cacti_list = Cacti.objects.exclude(pk=cactus_id).filter(species_id=species_id)
        # select * from cactus_cacti where id!=1;
    except Cacti.DoesNotExist:        
        raise Http404("Cacti does not exist")

    
    

    return render(request, 'cactus/cacti_detail.html', {'cacti':cacti, 'cacti_list':cacti_list})


'''
def cacti_detail(request, species_id): 

    try:
        cacti = Cacti.objects.filter(species_id=species_id)      
    except Cacti.DoesNotExist:        
        raise Http404("Cacti does not exist")

    

    return render(request, 'cactus/cacti_detail.html', {'cacti':cacti, 'species_id':species_id})
'''
