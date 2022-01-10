"""concertBand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from registry import views as registryViews
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('events/',views.events, name='events'),
    path('materials/',views.materials, name='materials')
   
]

# Composer
urlpatterns += [
    path('composers/', registryViews.composers, name='composers'),
    path('<id>/delete_composer', registryViews.delete_composer, name='delete_composer'),
    path('create_composer/', registryViews.create_composer, name='create_composer'),
    path('<id>/detail_composer', registryViews.detail_composer, name='detail_composer'),
    path('<id>/update_composer', registryViews.update_composer, name='update_composer')
]

# Score Genre
urlpatterns += [
    path('score_genres/', registryViews.score_genres, name='score_genres'),
    path('<id>/delete_score_genre', registryViews.delete_score_genre, name='delete_score_genre'),
    path('create_score_genre/', registryViews.create_score_genre, name='create_score_genre'),
    path('<id>/detail_score_genre', registryViews.detail_score_genre, name='detail_score_genre'),
    path('<id>/update_score_genre', registryViews.update_score_genre, name='update_score_genre')
]

# Sheet Category
urlpatterns += [
    path('sheet_categories/', registryViews.sheet_categories, name='sheet_categories'),
    path('<id>/delete_sheet_category', registryViews.delete_sheet_category, name='delete_sheet_category'),
    path('create_sheet_category/', registryViews.create_sheet_category, name='create_sheet_category'),
    path('<id>/detail_sheet_category', registryViews.detail_sheet_category, name='detail_sheet_category'),
    path('<id>/update_sheet_category', registryViews.update_sheet_category, name='update_sheet_category')
]

urlpatterns += staticfiles_urlpatterns()

# Authentication
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),    
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)