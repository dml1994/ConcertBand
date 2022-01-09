from django.db import models
from django.shortcuts import render
from app import models
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    return render(request,'index.html')

def events(request):
    event_all = models.Event.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(event_all, 5)
    
    try:
        event_list = paginator.page(page)
    except PageNotAnInteger:
        event_list = paginator.page(1)
    except EmptyPage:
        event_list = paginator.page(paginator.num_pages)

    return render(request,'app/event_list.html',{'event_list': event_list})

def materials(request):
    material_all = models.Material.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(material_all, 5)

    try:
        material_list = paginator.page(page)
    except PageNotAnInteger:
        material_list = paginator.page(1)
    except EmptyPage:
        material_list = paginator.page(paginator.num_pages)

    return render(request,'app/material_list.html',{'material_list': material_list})
     
