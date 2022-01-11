from django.db import models
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from accounting import models, forms

# Ledger

def ledgers(request):
    ledgers_all = models.Ledger.objects.all().order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(ledgers_all, 5)

    try:
        ledgers_list = paginator.page(page)
    except PageNotAnInteger:
        ledgers_list = paginator.page(1)
    except EmptyPage:
        ledgers_list = paginator.page(paginator.num_pages)

    return render(request,'accounting/ledgers_list.html',{'ledgers_list': ledgers_list, 'show': len(ledgers_all) > 0})

def delete_ledger(request, id):

    context ={}
 
    obj = get_object_or_404(models.Ledger, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/ledgers")
 
    return render(request, "accounting/delete_ledger.html", context)

def create_ledger(request):

    context ={}

    form = forms.LedgerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/ledgers")
 
    context['form']= form
    return render(request, "accounting/create_ledger.html", context)

def detail_ledger(request, id):

    context ={}

    context["data"] = models.Ledger.objects.get(id = id)

    return render(request, "accounting/detail_ledger.html", context)

def update_ledger(request, id):

    context ={}

    obj = get_object_or_404(models.Ledger, id = id)
 
    form = forms.LedgerForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.Ledger.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_ledger")
 
    context["form"] = form
 
    return render(request, "accounting/update_ledger.html", context)

# Period

def periods(request):
    periods_all = models.Period.objects.all().order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(periods_all, 5)

    try:
        periods_list = paginator.page(page)
    except PageNotAnInteger:
        periods_list = paginator.page(1)
    except EmptyPage:
        periods_list = paginator.page(paginator.num_pages)

    return render(request,'accounting/periods_list.html',{'periods_list': periods_list, 'show': len(periods_all) > 0})

def delete_period(request, id):

    context ={}
 
    obj = get_object_or_404(models.Period, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/periods")
 
    return render(request, "accounting/delete_period.html", context)

def create_period(request):

    context ={}

    form = forms.PeriodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/periods")
 
    context['form']= form
    return render(request, "accounting/create_period.html", context)

def detail_period(request, id):

    context ={}

    context["data"] = models.Period.objects.get(id = id)

    return render(request, "accounting/detail_period.html", context)

def update_period(request, id):

    context ={}

    obj = get_object_or_404(models.Period, id = id)
 
    form = forms.PeriodForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.Period.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_period")
 
    context["form"] = form
 
    return render(request, "accounting/update_period.html", context)

# Entry

def entries(request):
    entries_all = models.Entry.objects.all().order_by('date')

    page = request.GET.get('page', 1)
    paginator = Paginator(entries_all, 5)

    try:
        entries_list = paginator.page(page)
    except PageNotAnInteger:
        entries_list = paginator.page(1)
    except EmptyPage:
        entries_list = paginator.page(paginator.num_pages)

    return render(request,'accounting/entries_list.html',{'entries_list': entries_list, 'show': len(entries_all) > 0})

def delete_entry(request, id):

    context ={}
 
    obj = get_object_or_404(models.Entry, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/entries")
 
    return render(request, "accounting/delete_entry.html", context)

def create_entry(request):

    context ={}

    form = forms.EntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/entries")
 
    context['form']= form
    return render(request, "accounting/create_entry.html", context)

def detail_entry(request, id):

    context ={}

    context["data"] = models.Entry.objects.get(id = id)

    return render(request, "accounting/detail_entry.html", context)

def update_entry(request, id):

    context ={}

    obj = get_object_or_404(models.Entry, id = id)
 
    form = forms.EntryForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.Entry.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_entry")
 
    context["form"] = form
 
    return render(request, "accounting/update_entry.html", context)
