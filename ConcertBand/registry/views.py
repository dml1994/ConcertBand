from django.db import models
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from registry import models
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def sheet_categories(request):
    sheet_categories_all = models.SheetCategory.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(sheet_categories_all, 5)

    try:
        sheet_categories_list = paginator.page(page)
    except PageNotAnInteger:
        sheet_categories_list = paginator.page(1)
    except EmptyPage:
        sheet_categories_list = paginator.page(paginator.num_pages)

    return render(request,'registry/sheet_categories_list.html',{'sheet_categories_list': sheet_categories_list})

def delete_sheet_category(request, id):

    context ={}
 
    obj = get_object_or_404(models.SheetCategory, id = id)
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/sheet_categories")
 
    return render(request, "registry/delete_sheet_category.html", context)
