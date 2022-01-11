from django.db import models
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from registry import models
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from registry import forms


# Composers

def composers(request):
    composers_all = models.Composer.objects.all().order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(composers_all, 5)

    try:
        composers_list = paginator.page(page)
    except PageNotAnInteger:
        composers_list = paginator.page(1)
    except EmptyPage:
        composers_list = paginator.page(paginator.num_pages)

    return render(request,'registry/composers_list.html',{'composers_list': composers_list, 'show': len(composers_all) > 0})

def delete_composer(request, id):

    context ={}
 
    obj = get_object_or_404(models.Composer, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/composers")
 
    return render(request, "registry/delete_composer.html", context)

def create_composer(request):

    context ={}

    form = forms.ComposerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/composers")
 
    context['form']= form
    return render(request, "registry/create_composer.html", context)

def detail_composer(request, id):
  
    context ={}
 
    context["data"] = models.Composer.objects.get(id = id)
         
    return render(request, "registry/detail_composer.html", context)

def update_composer(request, id):

    context ={}

    obj = get_object_or_404(models.Composer, id = id)
 
    form = forms.ComposerForm(request.POST or None, request.FILES or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.Composer.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_composer")
 
    context["form"] = form
 
    return render(request, "registry/update_composer.html", context)

# Score

def scores(request):
    scores_all = models.Score.objects.all().order_by('title')

    page = request.GET.get('page', 1)
    paginator = Paginator(scores_all, 5)

    try:
        scores_list = paginator.page(page)
    except PageNotAnInteger:
        scores_list = paginator.page(1)
    except EmptyPage:
        scores_list = paginator.page(paginator.num_pages)

    return render(request,'registry/scores_list.html',{'scores_list': scores_list, 'show': len(scores_all) > 0})

def delete_score(request, id):

    context ={}
 
    obj = get_object_or_404(models.Score, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/scores")
 
    return render(request, "registry/delete_score.html", context)

def create_score(request):

    context ={}

    form = forms.ScoreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/scores")
 
    context['form']= form
    return render(request, "registry/create_score.html", context)

def detail_score(request, id):

    context ={}

    context["data"] = models.Score.objects.get(id = id)

    sheets_all = models.Sheet.objects.all().filter(score = context["data"])

    page = request.GET.get('page', 1)
    paginator = Paginator(sheets_all, 5)

    try:
        context["sheets_list"] = paginator.page(page)
    except PageNotAnInteger:
        context["sheets_list"] = paginator.page(1)
    except EmptyPage:
        context["sheets_list"] = paginator.page(paginator.num_pages)

    context["show"] =  len(sheets_all) > 0

    return render(request, "registry/detail_score.html", context)

def update_score(request, id):

    context ={}

    obj = get_object_or_404(models.Score, id = id)
 
    form = forms.ScoreForm(request.POST or None, request.FILES or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.Score.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_score")
 
    context["form"] = form
 
    return render(request, "registry/update_score.html", context)

# Score Genre

def score_genres(request):
    score_genres_all = models.ScoreGenre.objects.all().order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(score_genres_all, 5)

    try:
        score_genres_list = paginator.page(page)
    except PageNotAnInteger:
        score_genres_list = paginator.page(1)
    except EmptyPage:
        score_genres_list = paginator.page(paginator.num_pages)

    return render(request,'registry/score_genres_list.html',{'score_genres_list': score_genres_list, 'show': len(score_genres_all) > 0})

def delete_score_genre(request, id):

    context ={}
 
    obj = get_object_or_404(models.ScoreGenre, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/score_genres")
 
    return render(request, "registry/delete_score_genre.html", context)

def create_score_genre(request):

    context ={}

    form = forms.ScoreGenreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/score_genres")
 
    context['form']= form
    return render(request, "registry/create_score_genre.html", context)

def detail_score_genre(request, id):
  
    context ={}
 
    context["data"] = models.ScoreGenre.objects.get(id = id)
         
    return render(request, "registry/detail_score_genre.html", context)

def update_score_genre(request, id):

    context ={}

    obj = get_object_or_404(models.ScoreGenre, id = id)
 
    form = forms.ScoreGenreForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.ScoreGenre.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_score_genre")
 
    context["form"] = form
 
    return render(request, "registry/update_score_genre.html", context)

# Sheet

def sheets(request):
    sheets_all = models.Sheet.objects.all().order_by('score')

    page = request.GET.get('page', 1)
    paginator = Paginator(sheets_all, 5)

    try:
        sheets_list = paginator.page(page)
    except PageNotAnInteger:
        sheets_list = paginator.page(1)
    except EmptyPage:
        sheets_list = paginator.page(paginator.num_pages)

    return render(request,'registry/sheets_list.html',{'sheets_list': sheets_list, 'show': len(sheets_all) > 0})

def delete_sheet(request, id):

    context ={}
 
    obj = get_object_or_404(models.Sheet, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/sheets")
 
    return render(request, "registry/delete_sheet.html", context)

def create_sheet(request):

    context ={}

    form = forms.SheetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/sheets")
 
    context['form']= form
    return render(request, "registry/create_sheet.html", context)

def detail_sheet(request, id):

    context ={}

    context["data"] = models.Sheet.objects.get(id = id)
         
    return render(request, "registry/detail_sheet.html", context)

def update_sheet(request, id):

    context ={}

    obj = get_object_or_404(models.Sheet, id = id)
 
    form = forms.SheetForm(request.POST or None, request.FILES or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.Sheet.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_sheet")
 
    context["form"] = form
 
    return render(request, "registry/update_sheet.html", context)


# Sheet Category

def sheet_categories(request):
    sheet_categories_all = models.SheetCategory.objects.all().order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(sheet_categories_all, 5)

    try:
        sheet_categories_list = paginator.page(page)
    except PageNotAnInteger:
        sheet_categories_list = paginator.page(1)
    except EmptyPage:
        sheet_categories_list = paginator.page(paginator.num_pages)

    return render(request,'registry/sheet_categories_list.html',{'sheet_categories_list': sheet_categories_list, 'show': len(sheet_categories_all) > 0})

def delete_sheet_category(request, id):

    context ={}
 
    obj = get_object_or_404(models.SheetCategory, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/sheet_categories")
 
    return render(request, "registry/delete_sheet_category.html", context)

def create_sheet_category(request):

    context ={}

    form = forms.SheetCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/sheet_categories")
 
    context['form']= form
    return render(request, "registry/create_sheet_category.html", context)

def detail_sheet_category(request, id):

    context ={}

    context["data"] = models.SheetCategory.objects.get(id = id)
         
    return render(request, "registry/detail_sheet_category.html", context)

def update_sheet_category(request, id):

    context ={}

    obj = get_object_or_404(models.SheetCategory, id = id)
 
    form = forms.SheetCategoryForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.SheetCategory.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_sheet_category")
 
    context["form"] = form
 
    return render(request, "registry/update_sheet_category.html", context)


# VideoMedia

def video_medias(request):
    video_medias_all = models.VideoMedia.objects.all().order_by('title')

    page = request.GET.get('page', 1)
    paginator = Paginator(video_medias_all, 5)

    try:
        video_medias_list = paginator.page(page)
    except PageNotAnInteger:
        video_medias_list = paginator.page(1)
    except EmptyPage:
        video_medias_list = paginator.page(paginator.num_pages)

    return render(request,'registry/video_medias_list.html',{'video_medias_list': video_medias_list, 'show': len(video_medias_all) > 0})

def delete_video_media(request, id):

    context ={}
 
    obj = get_object_or_404(models.VideoMedia, id = id)
 
    if request.method =="POST":
       
        obj.delete()
      
        return HttpResponseRedirect("/video_medias")
 
    return render(request, "registry/delete_video_media.html", context)

def create_video_media(request):

    context ={}

    form = forms.VideoMediaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/video_medias")
 
    context['form']= form
    return render(request, "registry/create_video_media.html", context)

def detail_video_media(request, id):

    context ={}

    context["data"] = models.VideoMedia.objects.get(id = id)
         
    return render(request, "registry/detail_video_media.html", context)

def update_video_media(request, id):

    context ={}

    obj = get_object_or_404(models.VideoMedia, id = id)
 
    form = forms.VideoMediaForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        context["data"] = models.VideoMedia.objects.get(id = id)
        return HttpResponseRedirect("/"+id+"/detail_video_media")
 
    context["form"] = form
 
    return render(request, "registry/update_video_media.html", context)