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
from accounting import views as accountingViews
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

# Entry
urlpatterns += [
    path('entries/', accountingViews.entries, name='entries'),
    path('<id>/delete_entry', accountingViews.delete_entry, name='delete_entry'),
    path('create_entry/', accountingViews.create_entry, name='create_entry'),
    path('<id>/detail_entry', accountingViews.detail_entry, name='detail_entry'),
    path('<id>/update_entry', accountingViews.update_entry, name='update_entry')
]

# Ledger
urlpatterns += [
    path('ledgers/', accountingViews.ledgers, name='ledgers'),
    path('<id>/delete_ledger', accountingViews.delete_ledger, name='delete_ledger'),
    path('create_ledger/', accountingViews.create_ledger, name='create_ledger'),
    path('<id>/detail_ledger', accountingViews.detail_ledger, name='detail_ledger'),
    path('<id>/update_ledger', accountingViews.update_ledger, name='update_ledger')
]

# Period
urlpatterns += [
    path('periods/', accountingViews.periods, name='periods'),
    path('<id>/delete_period', accountingViews.delete_period, name='delete_period'),
    path('create_period/', accountingViews.create_period, name='create_period'),
    path('<id>/detail_period', accountingViews.detail_period, name='detail_period'),
    path('<id>/update_period', accountingViews.update_period, name='update_period')
]

# Score
urlpatterns += [
    path('scores/', registryViews.scores, name='scores'),
    path('<id>/delete_score', registryViews.delete_score, name='delete_score'),
    path('create_score/', registryViews.create_score, name='create_score'),
    path('<id>/detail_score', registryViews.detail_score, name='detail_score'),
    path('<id>/update_score', registryViews.update_score, name='update_score')
]

# Score Genre
urlpatterns += [
    path('score_genres/', registryViews.score_genres, name='score_genres'),
    path('<id>/delete_score_genre', registryViews.delete_score_genre, name='delete_score_genre'),
    path('create_score_genre/', registryViews.create_score_genre, name='create_score_genre'),
    path('<id>/detail_score_genre', registryViews.detail_score_genre, name='detail_score_genre'),
    path('<id>/update_score_genre', registryViews.update_score_genre, name='update_score_genre')
]

# Sheet
urlpatterns += [
    path('sheets/', registryViews.sheets, name='sheets'),
    path('<id>/delete_sheet', registryViews.delete_sheet, name='delete_sheet'),
    path('create_sheet/', registryViews.create_sheet, name='create_sheet'),
    path('<id>/detail_sheet', registryViews.detail_sheet, name='detail_sheet'),
    path('<id>/update_sheet', registryViews.update_sheet, name='update_sheet')
]

# Sheet Category
urlpatterns += [
    path('sheet_categories/', registryViews.sheet_categories, name='sheet_categories'),
    path('<id>/delete_sheet_category', registryViews.delete_sheet_category, name='delete_sheet_category'),
    path('create_sheet_category/', registryViews.create_sheet_category, name='create_sheet_category'),
    path('<id>/detail_sheet_category', registryViews.detail_sheet_category, name='detail_sheet_category'),
    path('<id>/update_sheet_category', registryViews.update_sheet_category, name='update_sheet_category')
]

# Video Media
urlpatterns += [
    path('video_medias/', registryViews.video_medias, name='video_medias'),
    path('<id>/delete_video_media', registryViews.delete_video_media, name='delete_video_media'),
    path('create_video_media/', registryViews.create_video_media, name='create_video_media'),
    path('<id>/detail_video_media', registryViews.detail_video_media, name='detail_video_media'),
    path('<id>/update_video_media', registryViews.update_video_media, name='update_video_media')
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