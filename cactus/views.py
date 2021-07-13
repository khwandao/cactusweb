from django.http import HttpResponse, Http404
from django.template import loader
from .models import Species, Cacti
from django.shortcuts import render


from matplotlib import pyplot as plt
import numpy as np
import base64
from io import BytesIO


def home(request):
    species_list = Species.objects.order_by('name')

    template = loader.get_template('cactus/home.html')
    context = {
        'species_list': species_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, species_id):
    color_type = []
    green_type = []
    other_type = []

    try:
        cacti = Cacti.objects.filter(species_id=species_id)     
    except Cacti.DoesNotExist:        
        raise Http404("Cacti does not exist")

    
    for item in cacti:
        species_name = item.species_id.name + " Page"
        break

    # Get color type list
    for item in cacti:        
        if item.color_type_id_id == 1:
            color_type.append(item)
        elif item.color_type_id_id == 2:
            green_type.append(item)
        else:
            other_type.append(item)
    
    template = loader.get_template('cactus/detail.html')
    context = {
        'color_type': color_type,
        'green_type': green_type,
        'other_type': other_type,   
        'cacti': cacti,
        'species_name': species_name,
    }

    return HttpResponse(template.render(context, request))


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


def chart(request):
    cacti_list = Cacti.objects.all()
    gymno_amount = 0
    astro_amount = 0
    
    for specie in cacti_list:
        if specie.species_id_id == 1:
            gymno_amount += 1
        else:
            astro_amount += 1
            
    template = loader.get_template('cactus/chart.html')

    # กำหนดขนาดกราฟ
    fig = plt.figure(figsize=(4, 4))

    # กำหนดชื่อให้กราฟ
    plt.title('Species')
    plt.ylabel('Quantity')

    # กำหนดข้อมูลที่แสดงในกราฟ
    species = ['#Gymno', '#Astro']
        
    quantity = [gymno_amount, astro_amount]

    # กำหนดแท่งกราฟ
    y_pos = np.arange(len(species))	
    plt.bar(y_pos, quantity, align='edge', width=0.3, color=('green','red'))
    plt.xticks(y_pos, species)	

    # กำหนดแกน Y ให้เป็นเลขจำนวนเต็ม
    loc, labels = plt.yticks()
    plt.yticks(np.arange(0, max(loc), step=1))

    # เซฟรูปลงในบัฟเฟอร์เพื่อส่งค่าไปที่ไฟล์เท็มเพลท
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'graphic': graphic
    }
    return HttpResponse(template.render(context, request))


def cactus_page(request):
    return render(request, 'cactus/cactus_page.html', {'name':'hello'})

    